grammar EmojiLang;

program: statement+ EOF;

statement
    : PRINT expr END                                  # PrintStmt
    | READ ID END                                     # ReadStmt
    | type ID ASSIGN expr END                          # VarDeclStmt
    | type ID ASSIGN LBRACK table_inside RBRACK END   # ArrayDeclStmt
    | ID ASSIGN expr END                               # AssignStmt
    | ID ASSIGN ID LBRACK INT RBRACK END        # ArrayAssignStmt
    | ID LBRACK INT RBRACK ASSIGN expr END #ArrayCellAssignStmt
    ;

table_inside
    : expr (COMMA table_inside)? 
    ;

expr
    : expr (MUL | DIV) expr          # MulDivExpr
    | expr (PLUS | MINUS) expr       # AddSubExpr
    | bool_type (AND | OR | XOR) bool_type     # LogicExpr
    | NEG bool_type                   # NegExpr
    | INT                             # IntExpr
    | FLOAT                           # FloatExpr
    | ID                              # IdExpr
    | ID LBRACK expr RBRACK           # ArrayAccessExpr
    | '(' expr ')'                    # ParensExpr
    | bool_type #BoolType

    ;

bool_type
    : TRUE # TrueExpr
    | FALSE # FalseExpr
    ;

// Typy danych jako emoji
type
    : INT_TYPE    # IntType
    | FLOAT_TYPE  # FloatType
    ;

// Typy danych
INT_TYPE:   '\uD83D\uDD22' ; // 🔢
FLOAT_TYPE: '\uD83D\uDC8E' ; // 💎

// Komendy i operatory
PRINT:  '\uD83D\uDDA8' '\uFE0F'?; // 🖨️
READ:   '\uD83D\uDCD6' '\uFE0F'?; // 📖
ASSIGN: '\u270D' '\uFE0F'?;       // ✍️
PLUS:   '\u2795';                 // ➕
MINUS:  '\u2796';                 // ➖
MUL:    '\u2716' '\uFE0F'?;       // ✖️
DIV:    '\u2797';                 // ➗
AND:    '\uD83E\uDD1D';           // 🤝
OR:     '\uD83D\uDD17';           // 🔗
XOR:    '\u274C';                 // ❌
NEG:    '\uD83D\uDEAB';           // 🚫
END:    '\uD83D\uDED1';           // 🛑
LBRACK: '\uD83D\uDC49';           // 👉
RBRACK: '\uD83D\uDC48';           // 👈
TRUE:   '\uD83D\uDC4D' ; // 👍 
FALSE:  '\uD83D\uDC4E' ; // 👎 

COMMA:  ',';
// Typy danych w lexerze
ID: [a-zA-Z]+ ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;

// Pomijanie białych znaków
WS: [ \t\r\n]+ -> skip ;