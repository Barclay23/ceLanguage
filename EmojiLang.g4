grammar EmojiLang;

program: statement+ ;

statement: PRINT expr END         # PrintStmt
         | ID ASSIGN expr END     # AssignStmt
         ;

expr: expr (MUL | DIV) expr       # MulDivExpr
    | expr (PLUS | MINUS) expr    # AddSubExpr
    | FLOAT                       # FloatExpr
    | INT                         # IntExpr
    | ID                          # IdExpr
    ;

//  LEXER (Terminalne słowa kluczowe i operatory w formie emotek) 
PRINT:  '🖨️' ;
ASSIGN: '👉' ;
PLUS:   '➕' ;
MINUS:  '➖' ;
MUL:    '✖️' ;
DIV:    '➗' ;
END:    '🛑' ;   // Zamiast nudnego średnika na końcu linii

//  LEXER (Typy danych) 
ID: [a-zA-Z]+ ;
INT: [0-9]+ ;
// Pamiętamy, że w języku polskim separatorem części ułamkowej jest przecinek, a nie kropka:
FLOAT: [0-9]+ ',' [0-9]+ ; 

WS: [ \t\r\n]+ -> skip ;