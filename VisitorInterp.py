from EmojiLangVisitor import EmojiLangVisitor
from EmojiLangParser import EmojiLangParser

class EmojiCompiler(EmojiLangVisitor):
    def __init__(self):
        self.headers = []
        self.user_functions = []
        self.main_body = []
        self.str_counter = 0

        self.ir_lines = self.headers
        self.register_counter = 1 

        self.variables = {}

        self._setup_llvm_headers()

    def get_new_reg(self):
        """Generuje nowy numer rejestru w LLVM (np. %1, %2)"""
        reg = f"%{self.register_counter}"
        self.register_counter += 1
        return reg

    def _setup_llvm_headers(self):
        """Przygotowuje zewnętrzne funkcje z języka C i strukturę pliku"""
        
        self.ir_lines.append("declare i32 @emoji_printf(i8*, ...)")
        self.ir_lines.append("declare i32 @emoji_scanf(i8*, ...)")
        self.ir_lines.append("declare void @exit(i32)")

        self.ir_lines.append('@fmt_out_int = private unnamed_addr constant [4 x i8] c"%d\\0A\\00"')
        self.ir_lines.append('@fmt_out_double = private unnamed_addr constant [5 x i8] c"%lf\\0A\\00"')

        self.ir_lines.append('@fmt_in_int = private unnamed_addr constant [3 x i8] c"%d\\00"')
        self.ir_lines.append('@fmt_in_double = private unnamed_addr constant [4 x i8] c"%lf\\00"')

        self.ir_lines.append('@fmt_out_str = private unnamed_addr constant [4 x i8] c"%s\\0A\\00"')
        self.ir_lines.append('@fmt_in_str = private unnamed_addr constant [3 x i8] c"%s\\00"')

    def finish(self):
        output = []
        output.extend(self.headers)
        if self.user_functions:
            
            output.extend(self.user_functions)

        output.append("define i32 @main() {")
        output.append("entry:")
        output.extend(self.main_body)
        output.append("  ret i32 0")
        output.append("}")
        
        return "\n".join(output)

    def _cast_to_type(self, val_data, target_type, line_num):
        current_type = val_data["type"]
        val = val_data["val"]

        if current_type == "array":
            raise Exception(f"Błąd semantyczny (Linia {line_num}): Nie można używać całej tablicy w wyrażeniach arytmetycznych!")
        
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

        else:
            raise Exception(f"Błąd semantyczny (Linia {line_num}): Nie można zrzutować {current_type} na {target_type}!")

    def _get_table_elements(self, ctx):
        """Funkcja rekurencyjnie wyciągająca elementy z tablicy zdefiniowanej w parserze"""
        elements = []
        current = ctx
        while current is not None:
            elements.append(current.expr())
            current = current.table_inside()
        return elements

    # OBSŁUGA INSTRUKCJI (STATEMENTS)
    
    def visitProgram(self, ctx: EmojiLangParser.ProgramContext):
        
        for f in ctx.functionDecl():
            self.visit(f)

        self.ir_lines = self.main_body
        for s in ctx.statement():
            self.visit(s)
        return None

    def visitFunctionHeader(self, ctx: EmojiLangParser.FunctionHeaderContext):
        func_name = ctx.ID().getText()

        prev_ir = self.ir_lines
        prev_vars = self.variables.copy()
        prev_reg_count = self.register_counter

        func_lines = []
        self.ir_lines = func_lines
        self.variables = {} 
        self.register_counter = 1

        params_in = []
        allocs = []
        if ctx.paramList():
            p_names = self.visit(ctx.paramList())
            for name in p_names:
                params_in.append(f"i32 %{name}_in")
                allocs.append(f"  %{name} = alloca i32")
                allocs.append(f"  store i32 %{name}_in, i32* %{name}")
                self.variables[name] = {"type": "i32", "is_array": False}

        self.ir_lines.append(f"define i32 @{func_name}({', '.join(params_in)}) {{")
        self.ir_lines.append("entry:")
        self.ir_lines.extend(allocs)

        self.visit(ctx.block())

        if not self.ir_lines[-1].strip().startswith("ret"):
            self.ir_lines.append("  ret i32 0")
            
        self.ir_lines.append("}")

        self.user_functions.append("\n".join(self.ir_lines))
        self.ir_lines = prev_ir
        self.variables = prev_vars
        self.register_counter = prev_reg_count

    def visitIdList(self, ctx: EmojiLangParser.IdListContext):
        return [id_node.getText() for id_node in ctx.ID()]
    def visitBlockLabel(self, ctx: EmojiLangParser.BlockLabelContext):
        for s in ctx.statement():
            self.visit(s)

    def visitReturnStmt(self, ctx: EmojiLangParser.ReturnStmtContext):
        val_data = self.visit(ctx.expr())
        val_casted = self._cast_to_type(val_data, "i32", ctx.start.line)
        self.ir_lines.append(f"  ret i32 {val_casted}")

    def visitFuncCallExpr(self, ctx: EmojiLangParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        args_llvm = []
        
        if ctx.argList():
            args_data = self.visit(ctx.argList())
            for arg in args_data:
                
                v = self._cast_to_type(arg, "i32", ctx.start.line)
                args_llvm.append(f"i32 {v}")
        
        res_reg = self.get_new_reg()
        self.ir_lines.append(f"  {res_reg} = call i32 @{func_name}({', '.join(args_llvm)})")
        return {"val": res_reg, "type": "i32"}

    def visitArgumentList(self, ctx: EmojiLangParser.ArgumentListContext):
        return [self.visit(e) for e in ctx.expr()]
    
    def visitVarDeclStmt(self, ctx: EmojiLangParser.VarDeclStmtContext):
        var_type_emoji = ctx.type_().getText()
        var_name = ctx.ID().getText()

        if var_type_emoji == '🔢':
            llvm_type = "i32"
        elif var_type_emoji == '💎':
            llvm_type = "double"
        elif var_type_emoji == '💡':
            llvm_type = "i1"
        elif var_type_emoji == '📝':
            llvm_type = "i8*"
        else:
            raise Exception(f"Nieznany typ: {var_type_emoji}")

        self.variables[var_name] = {"type": llvm_type, "is_array": False, "size": 1}
        self.ir_lines.append(f"  %{var_name} = alloca {llvm_type}")
        
        val_data = self.visit(ctx.expr())
        val_casted = self._cast_to_type(val_data, llvm_type, ctx.start.line)
        self.ir_lines.append(f"  store {llvm_type} {val_casted}, {llvm_type}* %{var_name}")

    def visitAssignStmt(self, ctx: EmojiLangParser.AssignStmtContext):
        var_name = ctx.ID().getText()
        if var_name not in self.variables or self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Zmienna '{var_name}' nie jest poprawną zmienną prostą!")

        llvm_type = self.variables[var_name]["type"]
        val_data = self.visit(ctx.expr())
        val_casted = self._cast_to_type(val_data, llvm_type, ctx.start.line)
        self.ir_lines.append(f"  store {llvm_type} {val_casted}, {llvm_type}* %{var_name}")

    def visitIfElseStmt(self, ctx: EmojiLangParser.IfElseStmtContext):
        cond_data = self.visit(ctx.bool_expr())
        cond_val = cond_data["val"]

        if_id = self.register_counter
        self.register_counter += 1
        then_l = f"if_then_{if_id}"
        else_l = f"if_else_{if_id}"
        end_l = f"if_end_{if_id}"

        has_else = ctx.ELSE() is not None
        target_f = else_l if has_else else end_l

        self.ir_lines.append(f"  br i1 {cond_val}, label %{then_l}, label %{target_f}")

        self.ir_lines.append(f"\n{then_l}:")
        self.visit(ctx.block(0))
        self.ir_lines.append(f"  br label %{end_l}")

        if has_else:
            self.ir_lines.append(f"\n{else_l}:")
            self.visit(ctx.block(1))
            self.ir_lines.append(f"  br label %{end_l}")

        self.ir_lines.append(f"\n{end_l}:")

    def visitPrintStmt(self, ctx: EmojiLangParser.PrintStmtContext):
        val_data = self.visit(ctx.expr())
        llvm_type = val_data["type"]
        val = val_data["val"]

        if llvm_type == "array":
            var_name = val
            base_type = val_data["base_type"]
            size = val_data["size"]
            array_type = f"[{size} x {base_type}]"

            for i in range(size):
                cell_ptr = self.get_new_reg()
                self.ir_lines.append(f"  {cell_ptr} = getelementptr {array_type}, {array_type}* %{var_name}, i32 0, i32 {i}")
                
                val_reg = self.get_new_reg()
                self.ir_lines.append(f"  {val_reg} = load {base_type}, {base_type}* {cell_ptr}")
                
                fmt_ptr = self.get_new_reg()
                call_reg = self.get_new_reg()
                
                if base_type == "i32":
                    self.ir_lines.append(f"  {fmt_ptr} = bitcast [4 x i8]* @fmt_out_int to i8*")
                    self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, i32 {val_reg})")
                elif base_type == "double":
                    self.ir_lines.append(f"  {fmt_ptr} = bitcast [5 x i8]* @fmt_out_double to i8*")
                    self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, double {val_reg})")

        elif llvm_type == "i32":
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [4 x i8]* @fmt_out_int to i8*")
            
            call_reg = self.get_new_reg()
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, i32 {val})")

        elif llvm_type == "double":
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [5 x i8]* @fmt_out_double to i8*")
            
            call_reg = self.get_new_reg()
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, double {val})")

        elif llvm_type == "i1":
            int_val = self.get_new_reg()
            self.ir_lines.append(f"  {int_val} = zext i1 {val} to i32")
            
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [4 x i8]* @fmt_out_int to i8*")
            
            call_reg = self.get_new_reg()
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, i32 {int_val})")
        elif llvm_type == "i8*":
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [4 x i8]* @fmt_out_str to i8*")
            call_reg = self.get_new_reg()
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_printf(i8* {fmt_ptr}, i8* {val})")
            
        else:
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Nieobsługiwany typ {llvm_type} w print!")

    def visitReadStmt(self, ctx: EmojiLangParser.ReadStmtContext):
        var_name = ctx.ID().getText()
        
        if var_name not in self.variables or self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Nie można wczytać do '{var_name}'!")

        llvm_type = self.variables[var_name]["type"]

        if llvm_type == "i32":
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [3 x i8]* @fmt_in_int to i8*")
            call_reg = self.get_new_reg() 
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_scanf(i8* {fmt_ptr}, {llvm_type}* %{var_name})")
            
        elif llvm_type == "double":
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [4 x i8]* @fmt_in_double to i8*")
            call_reg = self.get_new_reg() 
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_scanf(i8* {fmt_ptr}, {llvm_type}* %{var_name})")
            
        elif llvm_type == "i8*":
            
            fmt_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {fmt_ptr} = bitcast [3 x i8]* @fmt_in_str to i8*")

            buf_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {buf_ptr} = alloca [256 x i8]")

            str_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {str_ptr} = bitcast [256 x i8]* {buf_ptr} to i8*")

            call_reg = self.get_new_reg()
            self.ir_lines.append(f"  {call_reg} = call i32 (i8*, ...) @emoji_scanf(i8* {fmt_ptr}, i8* {str_ptr})")

            self.ir_lines.append(f"  store i8* {str_ptr}, i8** %{var_name}")
            
        else:
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Nieobsługiwany typ do wczytywania: {llvm_type}!")

    def visitArrayDeclStmt(self, ctx: EmojiLangParser.ArrayDeclStmtContext):
        var_type_emoji = ctx.type_().getText()
        var_name = ctx.ID().getText()
        llvm_base_type = "i32" if var_type_emoji == '🔢' else "double"

        elements = self._get_table_elements(ctx.table_inside())
        size = len(elements)
        array_type = f"[{size} x {llvm_base_type}]"

        self.variables[var_name] = {"type": llvm_base_type, "is_array": True, "size": size}
        self.ir_lines.append(f"  %{var_name} = alloca {array_type}")

        for i, expr_ctx in enumerate(elements):
            val_data = self.visit(expr_ctx)
            val_casted = self._cast_to_type(val_data, llvm_base_type, ctx.start.line)
            
            cell_ptr = self.get_new_reg()
            self.ir_lines.append(f"  {cell_ptr} = getelementptr {array_type}, {array_type}* %{var_name}, i32 0, i32 {i}")
            self.ir_lines.append(f"  store {llvm_base_type} {val_casted}, {llvm_base_type}* {cell_ptr}")

    def visitArrayCellAssignStmt(self, ctx: EmojiLangParser.ArrayCellAssignStmtContext):
        var_name = ctx.ID().getText()
        idx_data = self.visit(ctx.expr(0))
        val_data = self.visit(ctx.expr(1))
        
        if var_name not in self.variables or not self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): '{var_name}' nie jest tablicą!")

        arr_info = self.variables[var_name]
        llvm_base_type = arr_info["type"]
        size = arr_info['size']
        array_type = f"[{size} x {llvm_base_type}]"

        idx_casted = self._cast_to_type(idx_data, "i32", ctx.start.line)
        val_casted = self._cast_to_type(val_data, llvm_base_type, ctx.start.line)

        cmp_reg = self.get_new_reg()
        err_block = f"bounds_err_{self.register_counter}"
        ok_block = f"bounds_ok_{self.register_counter}"

        self.ir_lines.append(f"  {cmp_reg} = icmp uge i32 {idx_casted}, {size}")
        self.ir_lines.append(f"  br i1 {cmp_reg}, label %{err_block}, label %{ok_block}")

        self.ir_lines.append(f"\n{err_block}:")
        self.ir_lines.append("  call void @exit(i32 1)")
        self.ir_lines.append("  unreachable")

        self.ir_lines.append(f"\n{ok_block}:")

        cell_ptr = self.get_new_reg()
        self.ir_lines.append(f"  {cell_ptr} = getelementptr {array_type}, {array_type}* %{var_name}, i32 0, i32 {idx_casted}")
        self.ir_lines.append(f"  store {llvm_base_type} {val_casted}, {llvm_base_type}* {cell_ptr}")

    def visitWhileStmt(self, ctx: EmojiLangParser.WhileStmtContext):
        loop_id = self.register_counter
        self.register_counter += 1
        
        cond_label = f"while_cond_{loop_id}"
        body_label = f"while_body_{loop_id}"
        end_label = f"while_end_{loop_id}"

        self.ir_lines.append(f"  br label %{cond_label}")

        self.ir_lines.append(f"\n{cond_label}:")
        cond_data = self.visit(ctx.bool_expr())
        self.ir_lines.append(f"  br i1 {cond_data['val']}, label %{body_label}, label %{end_label}")

        self.ir_lines.append(f"\n{body_label}:")
        self.visit(ctx.block())
        self.ir_lines.append(f"  br label %{cond_label}")

        self.ir_lines.append(f"\n{end_label}:")

    # OBSŁUGA WYRAŻEŃ (EXPRESSIONS)

    def visitIntExpr(self, ctx: EmojiLangParser.IntExprContext):
        return {"val": ctx.INT().getText(), "type": "i32"}

    def visitFloatExpr(self, ctx: EmojiLangParser.FloatExprContext):
        
        clean_val = ctx.FLOAT().getText().replace(',', '.')
        return {"val": clean_val, "type": "double"}

    def visitStringExpr(self, ctx: EmojiLangParser.StringExprContext):
        raw_text = ctx.STRING_LITERAL().getText()[1:-1]
        length = len(raw_text) + 1
        
        str_id = self.str_counter
        self.str_counter += 1
        str_name = f"@.str.lit.{str_id}"
        
        self.headers.append(f'{str_name} = private unnamed_addr constant [{length} x i8] c"{raw_text}\\00"')
        
        reg = self.get_new_reg()
        self.ir_lines.append(f"  {reg} = bitcast [{length} x i8]* {str_name} to i8*")
        return {"val": reg, "type": "i8*"}
    
    def visitIdExpr(self, ctx: EmojiLangParser.IdExprContext):
        var_name = ctx.ID().getText()

        if var_name not in self.variables:
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Niezadeklarowana zmienna '{var_name}'!")

        if self.variables[var_name]["is_array"]:
            return {
                "val": var_name, 
                "type": "array", 
                "base_type": self.variables[var_name]["type"],
                "size": self.variables[var_name]["size"]
            }

        llvm_type = self.variables[var_name]["type"]
        reg = self.get_new_reg()
        self.ir_lines.append(f"  {reg} = load {llvm_type}, {llvm_type}* %{var_name}")
        return {"val": reg, "type": llvm_type}

    def visitArrayAccessExpr(self, ctx: EmojiLangParser.ArrayAccessExprContext):
        var_name = ctx.ID().getText()
        idx_data = self.visit(ctx.expr())

        if var_name not in self.variables or not self.variables[var_name]["is_array"]:
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): '{var_name}' nie jest tablicą!")

        arr_info = self.variables[var_name]
        llvm_base_type = arr_info["type"]
        size = arr_info['size']
        array_type = f"[{size} x {llvm_base_type}]"
        
        idx_casted = self._cast_to_type(idx_data, "i32", ctx.start.line)

        cmp_reg = self.get_new_reg()
        err_block = f"bounds_err_{self.register_counter}"
        ok_block = f"bounds_ok_{self.register_counter}"

        self.ir_lines.append(f"  {cmp_reg} = icmp uge i32 {idx_casted}, {size}")
        self.ir_lines.append(f"  br i1 {cmp_reg}, label %{err_block}, label %{ok_block}")

        self.ir_lines.append(f"\n{err_block}:")
        self.ir_lines.append("  call void @exit(i32 1)")
        self.ir_lines.append("  unreachable")

        self.ir_lines.append(f"\n{ok_block}:")
        
        cell_ptr = self.get_new_reg()
        self.ir_lines.append(f"  {cell_ptr} = getelementptr {array_type}, {array_type}* %{var_name}, i32 0, i32 {idx_casted}")
        
        val_reg = self.get_new_reg()
        self.ir_lines.append(f"  {val_reg} = load {llvm_base_type}, {llvm_base_type}* {cell_ptr}")
        return {"val": val_reg, "type": llvm_base_type}

    def visitAddSubExpr(self, ctx: EmojiLangParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        target_type = "double" if left["type"] == "double" or right["type"] == "double" else "i32"
        l_val = self._cast_to_type(left, target_type, ctx.start.line)
        r_val = self._cast_to_type(right, target_type, ctx.start.line)

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
        l_val = self._cast_to_type(left, target_type, ctx.start.line)
        r_val = self._cast_to_type(right, target_type, ctx.start.line)

        reg = self.get_new_reg()
        if ctx.MUL():
            op = "fmul" if target_type == "double" else "mul"
        else:
            op = "fdiv" if target_type == "double" else "sdiv"
            
        self.ir_lines.append(f"  {reg} = {op} {target_type} {l_val}, {r_val}")
        return {"val": reg, "type": target_type}

    def visitLogicExpr(self, ctx: EmojiLangParser.LogicExprContext):
        
        if ctx.XOR():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            
            if left["type"] != "i1" or right["type"] != "i1":
                raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Operacje logiczne są dozwolone wyłącznie na flagach prawda/fałsz!")
                
            reg = self.get_new_reg()
            self.ir_lines.append(f"  {reg} = xor i1 {left['val']}, {right['val']}")
            return {"val": reg, "type": "i1"}

        logic_id = self.register_counter
        self.register_counter += 1
        
        right_label = f"eval_right_{logic_id}"
        end_label = f"logic_end_{logic_id}"

        res_ptr = self.get_new_reg()
        self.ir_lines.append(f"  {res_ptr} = alloca i1")

        left = self.visit(ctx.expr(0))
        if left["type"] != "i1":
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Operacje logiczne są dozwolone wyłącznie na flagach prawda/fałsz!")

        self.ir_lines.append(f"  store i1 {left['val']}, i1* {res_ptr}")

        if ctx.AND():
            self.ir_lines.append(f"  br i1 {left['val']}, label %{right_label}, label %{end_label}")
        elif ctx.OR():
            self.ir_lines.append(f"  br i1 {left['val']}, label %{end_label}, label %{right_label}")

        self.ir_lines.append(f"\n{right_label}:")
        right = self.visit(ctx.expr(1))
        
        if right["type"] != "i1":
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Operacje logiczne są dozwolone wyłącznie na flagach prawda/fałsz!")

        self.ir_lines.append(f"  store i1 {right['val']}, i1* {res_ptr}")
        self.ir_lines.append(f"  br label %{end_label}")

        self.ir_lines.append(f"\n{end_label}:")
        final_res = self.get_new_reg()
        self.ir_lines.append(f"  {final_res} = load i1, i1* {res_ptr}")
        
        return {"val": final_res, "type": "i1"}

    def visitNegExpr(self, ctx: EmojiLangParser.NegExprContext):
        val = self.visit(ctx.expr())

        if val["type"] != "i1":
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Negacja (🚫) wymaga wartości prawda/fałsz!")

        reg = self.get_new_reg()
        self.ir_lines.append(f"  {reg} = xor i1 {val['val']}, 1")
        return {"val": reg, "type": "i1"}

    def visitTrueExpr(self, ctx: EmojiLangParser.TrueExprContext):
        return {"val": "1", "type": "i1"}

    def visitFalseExpr(self, ctx: EmojiLangParser.FalseExprContext):
        return {"val": "0", "type": "i1"}

    def visitCompare(self, ctx: EmojiLangParser.CompareContext):
        left_data = self.visit(ctx.expr(0))
        right_data = self.visit(ctx.expr(1))

        if left_data["type"] == "double" or right_data["type"] == "double":
            target_type = "double"
        else:
            target_type = "i32"

        val_l = self._cast_to_type(left_data, target_type,ctx.start.line )
        val_r = self._cast_to_type(right_data, target_type, ctx.start.line)

        res_reg = self.get_new_reg()
        operator = ctx.getChild(1).getText()

        if target_type == "i32":

            op_map = {">": "sgt", "<": "slt", "==": "eq"}
            instr = "icmp"
            llvm_op = op_map[operator]
        else:

            op_map = {">": "ogt", "<": "olt", "==": "oeq"}
            instr = "fcmp"
            llvm_op = op_map[operator]

        self.ir_lines.append(f"  {res_reg} = {instr} {llvm_op} {target_type} {val_l}, {val_r}")
        return {"val": res_reg, "type": "i1"}

    def visitBoolValueExpr(self, ctx: EmojiLangParser.BoolValueExprContext):
        result = self.visit(ctx.expr())

        if result["type"] != "i1":
            raise Exception(f"Błąd semantyczny (Linia {ctx.start.line}): Oczekiwano typu logicznego (i1), otrzymano {result['type']}")
            
        return result
    
    def visitBlockLabel(self, ctx: EmojiLangParser.BlockLabelContext):
        for s in ctx.statement():
            self.visit(s)