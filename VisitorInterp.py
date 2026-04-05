from EmojiLangVisitor import EmojiLangVisitor
from EmojiLangParser import EmojiLangParser

class MyEmojiCompiler(EmojiLangVisitor):
    def __init__(self):
        self.ir_lines = []
        self.register_counter = 1 
        
        # Słownik do zapamiętywania struktury zmiennych
        # Format: "nazwa": {"type": "i32", "is_array": False, "size": 1}
        self.variables = {}

        self._setup_llvm_headers()

    def get_new_reg(self):
        """Generuje nowy numer rejestru w LLVM (np. %1, %2)"""
        reg = f"%{self.register_counter}"
        self.register_counter += 1
        return reg

    def _setup_llvm_headers(self):
        """Przygotowuje zewnętrzne funkcje z języka C i strukturę pliku"""
        self.ir_lines.append("; --- NAGŁÓWKI I STAŁE ---")
        self.ir_lines.append("declare i32 @emoji_printf(i8*, ...)")
        self.ir_lines.append("declare i32 @emoji_scanf(i8*, ...)")
        self.ir_lines.append("declare void @exit(i32)")

        # Formatowanie dla printf (dodaje nową linię \0A)
        self.ir_lines.append('@fmt_out_int = private unnamed_addr constant [4 x i8] c"%d\\0A\\00"')
        self.ir_lines.append('@fmt_out_double = private unnamed_addr constant [5 x i8] c"%lf\\0A\\00"')
        
        # Formatowanie dla scanf (bez nowej linii)
        self.ir_lines.append('@fmt_in_int = private unnamed_addr constant [3 x i8] c"%d\\00"')
        self.ir_lines.append('@fmt_in_double = private unnamed_addr constant [4 x i8] c"%lf\\00"')
        
        self.ir_lines.append("\n; --- GŁÓWNY PROGRAM ---")
        self.ir_lines.append("define i32 @main() {")
        self.ir_lines.append("entry:")

    def finish(self):
        """Zamyka funkcję main poleceniem return 0"""
        self.ir_lines.append("  ret i32 0")
        self.ir_lines.append("}")
        return "\n".join(self.ir_lines)

    def _cast_to_type(self, val_data, target_type):
        """Wyrównuje typy (np. konwertuje i32 na double, jeśli wymaga tego działanie lub print)"""
        current_type = val_data["type"]
        val = val_data["val"]

        if current_type == target_type:
            return val

        new_reg = self.get_new_reg()

        if current_type == "i32" and target_type == "double":
            self.ir_lines.append(f"  {new_reg} = sitofp i32 {val} to double")
            return new_reg
        elif current_type == "double" and target_type == "i32":
            self.ir_lines.append(f"  {new_reg} = fptosi double {val} to i32")
            return new_reg
        elif current_type == "i1" and target_type == "i32":
            self.ir_lines.append(f"  {new_reg} = zext i1 {val} to i32")
            return new_reg
        elif current_type == "i32" and target_type == "i1":
            self.ir_lines.append(f"  {new_reg} = icmp ne i32 {val}, 0") # Wszystko co nie jest 0 to prawda
            return new_reg
        
        else:
            raise Exception(f"Błąd semantyczny: Nie można zrzutować {current_type} na {target_type}!")

    def _get_table_elements(self, ctx):
        """Funkcja rekurencyjnie wyciągająca elementy z tablicy zdefiniowanej w parserze"""
        elements = []
        current = ctx
        while current is not None:
            elements.append(current.expr())
            current = current.table_inside()
        return elements

    # ==========================================
    # OBSŁUGA INSTRUKCJI (STATEMENTS)
    # ==========================================

    def visitVarDeclStmt(self, ctx: EmojiLangParser.VarDeclStmtContext):
        var_type_emoji = ctx.type_().getText()
        var_name = ctx.ID().getText()
        
        # Mapowanie emoji na typy LLVM
        if var_type_emoji == '🔢':
            llvm_type = "i32"
        elif var_type_emoji == '💎':
            llvm_type = "double"
        elif var_type_emoji == '💡':
            llvm_type = "i1"
        else:
            raise Exception(f"Nieznany typ: {var_type_emoji}")

        self.variables[var_name] = {"type": llvm_type, "is_array": False, "size": 1}
        self.ir_lines.append(f"  %{var_name} = alloca {llvm_type}")
        
        val_data = self.visit(ctx.expr())
        val_casted = self._cast_to_type(val_data, llvm_type)
        self.ir_lines.append(f"  store {llvm_type} {val_casted}, {llvm_type}* %{var_name}")

    def visitAssignStmt(self, ctx: EmojiLangParser.AssignStmtContext):
        var_name = ctx.ID().getText()
        if var_name not in self.variables or self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny: Zmienna '{var_name}' nie jest poprawną zmienną prostą!")

        llvm_type = self.variables[var_name]["type"]
        val_data = self.visit(ctx.expr())
        val_casted = self._cast_to_type(val_data, llvm_type)
        self.ir_lines.append(f"  store {llvm_type} {val_casted}, {llvm_type}* %{var_name}")

    
    def visitPrintStmt(self, ctx: EmojiLangParser.PrintStmtContext):
    # 1. Najpierw odwiedzamy wyrażenie (może wygenerować np. load %31)
        val_data = self.visit(ctx.expr())
        llvm_type = val_data["type"]
        val = val_data["val"]

        if llvm_type == "i32":
            # Pobieramy fmt_ptr i od razu wypisujemy instrukcję
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [4 x i8]* @fmt_out_int to i8*")
            
            # Pobieramy call_reg i od razu wypisujemy instrukcję
            call_reg = self.get_new_reg()
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, i32 {val})")

        elif llvm_type == "double":
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [5 x i8]* @fmt_out_double to i8*")
            
            call_reg = self.get_new_reg()
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, double {val})")

        elif llvm_type == "i1":
            # 1. Najpierw rzutowanie i1 -> i32 (pobiera nowy rejestr)
            int_val = self.get_new_reg()
            self.ir_lines.append(f"  {int_val} = zext i1 {val} to i32")
            
            # 2. Potem bitcast formatu (pobiera kolejny rejestr)
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [4 x i8]* @fmt_out_int to i8*")
            
            # 3. Na końcu wywołanie (pobiera kolejny rejestr)
            call_reg = self.get_new_reg()
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, i32 {int_val})")
        else:
            raise Exception(f"Błąd semantyczny: Nieobsługiwany typ {llvm_type} w print!")

    def visitReadStmt(self, ctx: EmojiLangParser.ReadStmtContext):
        var_name = ctx.ID().getText()
        if var_name not in self.variables or self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny: Nie można wczytać do '{var_name}'!")

        llvm_type = self.variables[var_name]["type"]
        fmt_ptr = self.get_new_reg()

        if llvm_type == "i32":
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [3 x i8]* @fmt_in_int to i8*")
        elif llvm_type == "double":
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [4 x i8]* @fmt_in_double to i8*")

        call_reg = self.get_new_reg() 
        self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_scanf(i8* {fmt_ptr}, {llvm_type}* %{var_name})")

    # --- OBSŁUGA TABLIC ---

    def visitArrayDeclStmt(self, ctx: EmojiLangParser.ArrayDeclStmtContext):
        var_type_emoji = ctx.type_().getText()
        var_name = ctx.ID().getText()
        llvm_base_type = "i32" if var_type_emoji == '🔢' else "double"

        elements = self._get_table_elements(ctx.table_inside())
        size = len(elements)
        array_type = f"[{size} x {llvm_base_type}]"

        self.variables[var_name] = {"type": llvm_base_type, "is_array": True, "size": size}
        self.ir_lines.append(f"  %{var_name} = alloca {array_type}")

        # Inicjalizacja komórek podanymi wartościami
        for i, expr_ctx in enumerate(elements):
            val_data = self.visit(expr_ctx)
            val_casted = self._cast_to_type(val_data, llvm_base_type)
            
            cell_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {cell_ptr} = getelementptr {array_type}, {array_type}* %{var_name}, i32 0, i32 {i}")
            self.ir_lines.append(f"  store {llvm_base_type} {val_casted}, {llvm_base_type}* {cell_ptr}")

    def visitArrayCellAssignStmt(self, ctx: EmojiLangParser.ArrayCellAssignStmtContext):
        var_name = ctx.ID().getText()
        idx_data = self.visit(ctx.expr(0))
        val_data = self.visit(ctx.expr(1))

        if var_name not in self.variables or not self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny: '{var_name}' nie jest tablicą!")

        arr_info = self.variables[var_name]
        llvm_base_type = arr_info["type"]
        size = arr_info['size']
        array_type = f"[{size} x {llvm_base_type}]"

        idx_casted = self._cast_to_type(idx_data, "i32")
        val_casted = self._cast_to_type(val_data, llvm_base_type)

        # --- BONUS: SPRAWDZANIE ZAKRESÓW (BOUNDARY CHECK) ---
        cmp_reg = self.get_new_reg()
        err_block = f"bounds_err_{self.register_counter}"
        ok_block = f"bounds_ok_{self.register_counter}"
        
        # icmp uge sprawdza, czy indeks jest ujemny LUB większy/równy rozmiarowi
        self.ir_lines.append(f"  {cmp_reg} = icmp uge i32 {idx_casted}, {size}")
        self.ir_lines.append(f"  br i1 {cmp_reg}, label %{err_block}, label %{ok_block}")
        
        # Blok błędu - awaryjne zamknięcie programu
        self.ir_lines.append(f"\n{err_block}:")
        self.ir_lines.append("  call void @exit(i32 1)")
        self.ir_lines.append("  unreachable")
        
        # Blok sukcesu - wykonujemy fizyczny zapis do pamięci
        self.ir_lines.append(f"\n{ok_block}:")

        cell_ptr = self.get_new_reg()
        self.ir_lines.append(f"  {cell_ptr} = getelementptr {array_type}, {array_type}* %{var_name}, i32 0, i32 {idx_casted}")
        self.ir_lines.append(f"  store {llvm_base_type} {val_casted}, {llvm_base_type}* {cell_ptr}")
    # ==========================================
    # OBSŁUGA WYRAŻEŃ (EXPRESSIONS)
    # ==========================================

    def visitIntExpr(self, ctx: EmojiLangParser.IntExprContext):
        return {"val": ctx.INT().getText(), "type": "i32"}

    def visitFloatExpr(self, ctx: EmojiLangParser.FloatExprContext):
        # Zamiana polskiego przecinka na kropkę, której oczekuje LLVM i Python
        clean_val = ctx.FLOAT().getText().replace(',', '.')
        return {"val": clean_val, "type": "double"}

    def visitIdExpr(self, ctx: EmojiLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        if var_name not in self.variables or self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny: Niezadeklarowana lub błędna zmienna '{var_name}'!")
            
        llvm_type = self.variables[var_name]["type"]
        reg = self.get_new_reg()
        self.ir_lines.append(f"  {reg} = load {llvm_type}, {llvm_type}* %{var_name}")
        return {"val": reg, "type": llvm_type}

    def visitArrayAccessExpr(self, ctx: EmojiLangParser.ArrayAccessExprContext):
        var_name = ctx.ID().getText()
        idx_data = self.visit(ctx.expr())

        if var_name not in self.variables or not self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny: '{var_name}' nie jest tablicą!")

        arr_info = self.variables[var_name]
        llvm_base_type = arr_info["type"]
        size = arr_info['size']
        array_type = f"[{size} x {llvm_base_type}]"
        
        idx_casted = self._cast_to_type(idx_data, "i32")

        # --- BONUS: SPRAWDZANIE ZAKRESÓW (BOUNDARY CHECK) ---
        cmp_reg = self.get_new_reg()
        err_block = f"bounds_err_{self.register_counter}"
        ok_block = f"bounds_ok_{self.register_counter}"
        
        # Sprawdzamy, czy indeks >= rozmiar tablicy (traktowane jako unsigned, więc łapie też ujemne)
        self.ir_lines.append(f"  {cmp_reg} = icmp uge i32 {idx_casted}, {size}")
        self.ir_lines.append(f"  br i1 {cmp_reg}, label %{err_block}, label %{ok_block}")
        
        # Blok błędu - zamykamy program
        self.ir_lines.append(f"\n{err_block}:")
        self.ir_lines.append("  call void @exit(i32 1)")
        self.ir_lines.append("  unreachable")
        
        # Blok sukcesu - kontynuujemy odczyt
        self.ir_lines.append(f"\n{ok_block}:")
        
        cell_ptr = self.get_new_reg()
        self.ir_lines.append(f"  {cell_ptr} = getelementptr {array_type}, {array_type}* %{var_name}, i32 0, i32 {idx_casted}")
        
        val_reg = self.get_new_reg()
        self.ir_lines.append(f"  {val_reg} = load {llvm_base_type}, {llvm_base_type}* {cell_ptr}")
        return {"val": val_reg, "type": llvm_base_type}

    def visitAddSubExpr(self, ctx: EmojiLangParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        # Ustalamy typ wynikowy (jeśli w działaniu jest ułamek, wszystko staje się ułamkiem)
        target_type = "double" if left["type"] == "double" or right["type"] == "double" else "i32"
        l_val = self._cast_to_type(left, target_type)
        r_val = self._cast_to_type(right, target_type)

        reg = self.get_new_reg()
        if ctx.PLUS():
            op = "fadd" if target_type == "double" else "add"
        else:
            op = "fsub" if target_type == "double" else "sub"
            
        self.ir_lines.append(f"  {reg} = {op} {target_type} {l_val}, {r_val}")
        return {"val": reg, "type": target_type}

    def visitMulDivExpr(self, ctx: EmojiLangParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        target_type = "double" if left["type"] == "double" or right["type"] == "double" else "i32"
        l_val = self._cast_to_type(left, target_type)
        r_val = self._cast_to_type(right, target_type)

        reg = self.get_new_reg()
        if ctx.MUL():
            op = "fmul" if target_type == "double" else "mul"
        else:
            op = "fdiv" if target_type == "double" else "sdiv"
            
        self.ir_lines.append(f"  {reg} = {op} {target_type} {l_val}, {r_val}")
        return {"val": reg, "type": target_type}

    def visitLogicExpr(self, ctx: EmojiLangParser.LogicExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        # Zamiast wyrzucać błąd, automatycznie rzutujemy wszystko na "i1" (bool) !
        l_val = self._cast_to_type(left, "i1")
        r_val = self._cast_to_type(right, "i1")

        reg = self.get_new_reg()
        if ctx.AND():
            self.ir_lines.append(f"  {reg} = and i1 {l_val}, {r_val}")
        elif ctx.OR():
            self.ir_lines.append(f"  {reg} = or i1 {l_val}, {r_val}")
        elif ctx.XOR():
            self.ir_lines.append(f"  {reg} = xor i1 {l_val}, {r_val}")

        return {"val": reg, "type": "i1"}

    def visitNegExpr(self, ctx: EmojiLangParser.NegExprContext):
        val = self.visit(ctx.expr())
        
        # Rzutujemy na i1, więc 🚫 a (gdzie a to liczba) też zadziała!
        bool_val = self._cast_to_type(val, "i1")

        reg = self.get_new_reg()
        self.ir_lines.append(f"  {reg} = xor i1 {bool_val}, 1")
        return {"val": reg, "type": "i1"}

    # --- Bool_type 👍 / 👎 ---
    def visitTrueExpr(self, ctx: EmojiLangParser.TrueExprContext):
        return {"val": "1", "type": "i1"}

    def visitFalseExpr(self, ctx: EmojiLangParser.FalseExprContext):
        return {"val": "0", "type": "i1"}
