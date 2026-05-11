grammar EmojiLang;

program
    : (structDecl | functionDecl | statement)* EOF
    ;
    
statement
    : PRINT expr END                                  # PrintStmt
    | READ ID END                                     # ReadStmt
    | scopeSpecifier? type ID ASSIGN expr END         # VarDeclStmt
    | scopeSpecifier? type ID ASSIGN LBRACK table_inside RBRACK END   # ArrayDeclStmt
    | ID ASSIGN expr END                               # AssignStmt
    | ID ASSIGN ID LBRACK INT RBRACK END        # ArrayAssignStmt
    | ID LBRACK expr RBRACK ASSIGN expr END #ArrayCellAssignStmt
    | IF bool_expr THEN COLON block (ELSE COLON block)? FI #IfElseStmt
    | WHILE bool_expr THEN COLON block FI        # WhileStmt
    | RETURN expr END                                 # ReturnStmt
    | ID DOT ID ASSIGN expr END                      # StructFieldAssignStmt
    | ID ID ASSIGN LBRACE structInitList? RBRACE END # StructInstStmt
    ;


structInitList
    : DOT ID ASSIGN expr (COMMA DOT ID ASSIGN expr)*
    ;

structDecl 
    : STRUCT ID LBRACE structField+ RBRACE END
    ;

structField
    : type ID END
    ;

table_inside
    : expr (COMMA table_inside)? 
    ;

expr
    : expr (MUL | DIV) expr          # MulDivExpr
    | expr (PLUS | MINUS) expr       # AddSubExpr
    | expr (AND | OR | XOR) expr     # LogicExpr 
    | NEG expr                       # NegExpr
    | INT                             # IntExpr
    | FLOAT                           # FloatExpr
    | TRUE                            # TrueExpr
    | FALSE                           # FalseExpr
    | ID                              # IdExpr
    | ID LBRACK expr RBRACK           # ArrayAccessExpr
    | ID LPAREN argList? RPAREN       # FuncCallExpr
    | STRING_LITERAL                  # StringExpr
    | '(' expr ')'                    # ParensExpr
    | ID DOT ID                       # StructAccessExpr
    ;

// int nieważne = func();

// func();

bool_expr
    : expr (GREATER | LESS | EQUALS) expr #compare
    | expr #BoolValueExpr
    ;

block
    : LBRACE statement+ RBRACE #BlockLabel
    ;

    
//{} block
//() funckaj
//[] tablica

functionDecl
    : FUNC ID LPAREN paramList? RPAREN COLON block #functionHeader
    ;

paramList
    : ID (COMMA ID)* #idList
    ;

argList
    : expr (COMMA expr)* #argumentList
    ;


// Typy danych jako emoji
type
    : INT_TYPE    # IntType
    | FLOAT_TYPE  # FloatType
    | BOOL_TYPE # BoolTypeDecl
    | STRING_TYPE # StringType
    ;

scopeSpecifier
    : GLOBAL
    | LOCAL
    ;

// Typy danych
INT_TYPE:   '\uD83D\uDD22' ; // 🔢
FLOAT_TYPE: '\uD83D\uDC8E' ; // 💎
BOOL_TYPE:  '\uD83D\uDCA1'; // 💡
STRING_TYPE: '\uD83D\uDCDD' ; // 📝
STRING_LITERAL: '"' ~["]* '"' ; // Tekst w cudzyslowach

GLOBAL: '\uD83C\uDF0D'; // 🌍
LOCAL:  '\uD83C\uDFE0'; // 🏠

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
//🫷🫸
LBRACE: '\uD83E\uDD1C'; // 🤜
RBRACE: '\uD83E\uDD1B'; // 🤛
STRUCT: '\uD83D\uDCE6'; // 📦
LPAREN: '\u270B'; // ✋
RPAREN: '\uD83E\uDD1A'; // 🤚

FUNC:   '\uD83E\uDDE9'; // 🧩
RETURN: '\uD83D\uDD19'; // 🔙


// IF / ELSE/WHILE
IF:     '\uD83E\uDD14';           // 🤔
THEN:   '\u27A1' '\uFE0F'?;       // ➡️
ELSE:   '\uD83D\uDD00';           // 🔀
COLON:  ':';
WHILE: '\uD83D\uDD01'; // 🔁
FI:     '\u2757';                 // ❗

//compare
GREATER: '>'; //GREATER
LESS: '<'; //LESS
EQUALS: '==';//EQUALS


//FOR
DOT: '.';
COMMA:  ',';
// Typy danych w lexerze
ID: [a-zA-Z]+ ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;

// Pomijanie białych znaków
WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;