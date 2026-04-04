# Generated from EmojiLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,61,8,1,1,2,1,2,1,2,3,2,66,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,88,8,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,96,8,3,10,3,12,3,99,9,3,1,4,1,4,3,4,103,
        8,4,1,5,1,5,3,5,107,8,5,1,5,0,1,6,6,0,2,4,6,8,10,0,3,1,0,12,14,1,
        0,10,11,1,0,8,9,121,0,13,1,0,0,0,2,60,1,0,0,0,4,62,1,0,0,0,6,87,
        1,0,0,0,8,102,1,0,0,0,10,106,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,
        14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,
        0,0,1,18,1,1,0,0,0,19,20,5,5,0,0,20,21,3,6,3,0,21,22,5,16,0,0,22,
        61,1,0,0,0,23,24,5,6,0,0,24,25,5,22,0,0,25,61,5,16,0,0,26,27,3,10,
        5,0,27,28,5,22,0,0,28,29,5,7,0,0,29,30,3,6,3,0,30,31,5,16,0,0,31,
        61,1,0,0,0,32,33,3,10,5,0,33,34,5,22,0,0,34,35,5,7,0,0,35,36,5,17,
        0,0,36,37,3,4,2,0,37,38,5,18,0,0,38,39,5,16,0,0,39,61,1,0,0,0,40,
        41,5,22,0,0,41,42,5,7,0,0,42,43,3,6,3,0,43,44,5,16,0,0,44,61,1,0,
        0,0,45,46,5,22,0,0,46,47,5,7,0,0,47,48,5,22,0,0,48,49,5,17,0,0,49,
        50,5,23,0,0,50,51,5,18,0,0,51,61,5,16,0,0,52,53,5,22,0,0,53,54,5,
        17,0,0,54,55,5,23,0,0,55,56,5,18,0,0,56,57,5,7,0,0,57,58,3,6,3,0,
        58,59,5,16,0,0,59,61,1,0,0,0,60,19,1,0,0,0,60,23,1,0,0,0,60,26,1,
        0,0,0,60,32,1,0,0,0,60,40,1,0,0,0,60,45,1,0,0,0,60,52,1,0,0,0,61,
        3,1,0,0,0,62,65,3,6,3,0,63,64,5,21,0,0,64,66,3,4,2,0,65,63,1,0,0,
        0,65,66,1,0,0,0,66,5,1,0,0,0,67,68,6,3,-1,0,68,69,3,8,4,0,69,70,
        7,0,0,0,70,71,3,8,4,0,71,88,1,0,0,0,72,73,5,15,0,0,73,88,3,8,4,0,
        74,88,5,23,0,0,75,88,5,24,0,0,76,88,5,22,0,0,77,78,5,22,0,0,78,79,
        5,17,0,0,79,80,3,6,3,0,80,81,5,18,0,0,81,88,1,0,0,0,82,83,5,1,0,
        0,83,84,3,6,3,0,84,85,5,2,0,0,85,88,1,0,0,0,86,88,3,8,4,0,87,67,
        1,0,0,0,87,72,1,0,0,0,87,74,1,0,0,0,87,75,1,0,0,0,87,76,1,0,0,0,
        87,77,1,0,0,0,87,82,1,0,0,0,87,86,1,0,0,0,88,97,1,0,0,0,89,90,10,
        10,0,0,90,91,7,1,0,0,91,96,3,6,3,11,92,93,10,9,0,0,93,94,7,2,0,0,
        94,96,3,6,3,10,95,89,1,0,0,0,95,92,1,0,0,0,96,99,1,0,0,0,97,95,1,
        0,0,0,97,98,1,0,0,0,98,7,1,0,0,0,99,97,1,0,0,0,100,103,5,19,0,0,
        101,103,5,20,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,9,1,0,0,0,104,
        107,5,3,0,0,105,107,5,4,0,0,106,104,1,0,0,0,106,105,1,0,0,0,107,
        11,1,0,0,0,8,15,60,65,87,95,97,102,106
    ]

class EmojiLangParser ( Parser ):

    grammarFileName = "EmojiLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\uD83D\\uDD22'", "'\\uD83D\\uDC8E'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\u2795'", 
                     "'\\u2796'", "<INVALID>", "'\\u2797'", "'\\uD83E\\uDD1D'", 
                     "'\\uD83D\\uDD17'", "'\\u274C'", "'\\uD83D\\uDEAB'", 
                     "'\\uD83D\\uDED1'", "'\\uD83D\\uDC49'", "'\\uD83D\\uDC48'", 
                     "'\\uD83D\\uDC4D'", "'\\uD83D\\uDC4E'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INT_TYPE", 
                      "FLOAT_TYPE", "PRINT", "READ", "ASSIGN", "PLUS", "MINUS", 
                      "MUL", "DIV", "AND", "OR", "XOR", "NEG", "END", "LBRACK", 
                      "RBRACK", "TRUE", "FALSE", "COMMA", "ID", "INT", "FLOAT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_table_inside = 2
    RULE_expr = 3
    RULE_bool_type = 4
    RULE_type = 5

    ruleNames =  [ "program", "statement", "table_inside", "expr", "bool_type", 
                   "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INT_TYPE=3
    FLOAT_TYPE=4
    PRINT=5
    READ=6
    ASSIGN=7
    PLUS=8
    MINUS=9
    MUL=10
    DIV=11
    AND=12
    OR=13
    XOR=14
    NEG=15
    END=16
    LBRACK=17
    RBRACK=18
    TRUE=19
    FALSE=20
    COMMA=21
    ID=22
    INT=23
    FLOAT=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(EmojiLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EmojiLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(EmojiLangParser.StatementContext,i)


        def getRuleIndex(self):
            return EmojiLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = EmojiLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194424) != 0)):
                    break

            self.state = 17
            self.match(EmojiLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EmojiLangParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(EmojiLangParser.PRINT, 0)
        def expr(self):
            return self.getTypedRuleContext(EmojiLangParser.ExprContext,0)

        def END(self):
            return self.getToken(EmojiLangParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)


    class VarDeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(EmojiLangParser.TypeContext,0)

        def ID(self):
            return self.getToken(EmojiLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(EmojiLangParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(EmojiLangParser.ExprContext,0)

        def END(self):
            return self.getToken(EmojiLangParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclStmt" ):
                listener.enterVarDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclStmt" ):
                listener.exitVarDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclStmt" ):
                return visitor.visitVarDeclStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(EmojiLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(EmojiLangParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(EmojiLangParser.ExprContext,0)

        def END(self):
            return self.getToken(EmojiLangParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class ArrayCellAssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(EmojiLangParser.ID, 0)
        def LBRACK(self):
            return self.getToken(EmojiLangParser.LBRACK, 0)
        def INT(self):
            return self.getToken(EmojiLangParser.INT, 0)
        def RBRACK(self):
            return self.getToken(EmojiLangParser.RBRACK, 0)
        def ASSIGN(self):
            return self.getToken(EmojiLangParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(EmojiLangParser.ExprContext,0)

        def END(self):
            return self.getToken(EmojiLangParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayCellAssignStmt" ):
                listener.enterArrayCellAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayCellAssignStmt" ):
                listener.exitArrayCellAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayCellAssignStmt" ):
                return visitor.visitArrayCellAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class ArrayDeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(EmojiLangParser.TypeContext,0)

        def ID(self):
            return self.getToken(EmojiLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(EmojiLangParser.ASSIGN, 0)
        def LBRACK(self):
            return self.getToken(EmojiLangParser.LBRACK, 0)
        def table_inside(self):
            return self.getTypedRuleContext(EmojiLangParser.Table_insideContext,0)

        def RBRACK(self):
            return self.getToken(EmojiLangParser.RBRACK, 0)
        def END(self):
            return self.getToken(EmojiLangParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDeclStmt" ):
                listener.enterArrayDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDeclStmt" ):
                listener.exitArrayDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclStmt" ):
                return visitor.visitArrayDeclStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(EmojiLangParser.READ, 0)
        def ID(self):
            return self.getToken(EmojiLangParser.ID, 0)
        def END(self):
            return self.getToken(EmojiLangParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EmojiLangParser.ID)
            else:
                return self.getToken(EmojiLangParser.ID, i)
        def ASSIGN(self):
            return self.getToken(EmojiLangParser.ASSIGN, 0)
        def LBRACK(self):
            return self.getToken(EmojiLangParser.LBRACK, 0)
        def INT(self):
            return self.getToken(EmojiLangParser.INT, 0)
        def RBRACK(self):
            return self.getToken(EmojiLangParser.RBRACK, 0)
        def END(self):
            return self.getToken(EmojiLangParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssignStmt" ):
                listener.enterArrayAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssignStmt" ):
                listener.exitArrayAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssignStmt" ):
                return visitor.visitArrayAssignStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = EmojiLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = EmojiLangParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(EmojiLangParser.PRINT)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(EmojiLangParser.END)
                pass

            elif la_ == 2:
                localctx = EmojiLangParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(EmojiLangParser.READ)
                self.state = 24
                self.match(EmojiLangParser.ID)
                self.state = 25
                self.match(EmojiLangParser.END)
                pass

            elif la_ == 3:
                localctx = EmojiLangParser.VarDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.type_()
                self.state = 27
                self.match(EmojiLangParser.ID)
                self.state = 28
                self.match(EmojiLangParser.ASSIGN)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(EmojiLangParser.END)
                pass

            elif la_ == 4:
                localctx = EmojiLangParser.ArrayDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.type_()
                self.state = 33
                self.match(EmojiLangParser.ID)
                self.state = 34
                self.match(EmojiLangParser.ASSIGN)
                self.state = 35
                self.match(EmojiLangParser.LBRACK)
                self.state = 36
                self.table_inside()
                self.state = 37
                self.match(EmojiLangParser.RBRACK)
                self.state = 38
                self.match(EmojiLangParser.END)
                pass

            elif la_ == 5:
                localctx = EmojiLangParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.match(EmojiLangParser.ID)
                self.state = 41
                self.match(EmojiLangParser.ASSIGN)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(EmojiLangParser.END)
                pass

            elif la_ == 6:
                localctx = EmojiLangParser.ArrayAssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.match(EmojiLangParser.ID)
                self.state = 46
                self.match(EmojiLangParser.ASSIGN)
                self.state = 47
                self.match(EmojiLangParser.ID)
                self.state = 48
                self.match(EmojiLangParser.LBRACK)
                self.state = 49
                self.match(EmojiLangParser.INT)
                self.state = 50
                self.match(EmojiLangParser.RBRACK)
                self.state = 51
                self.match(EmojiLangParser.END)
                pass

            elif la_ == 7:
                localctx = EmojiLangParser.ArrayCellAssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.match(EmojiLangParser.ID)
                self.state = 53
                self.match(EmojiLangParser.LBRACK)
                self.state = 54
                self.match(EmojiLangParser.INT)
                self.state = 55
                self.match(EmojiLangParser.RBRACK)
                self.state = 56
                self.match(EmojiLangParser.ASSIGN)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(EmojiLangParser.END)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_insideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EmojiLangParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(EmojiLangParser.COMMA, 0)

        def table_inside(self):
            return self.getTypedRuleContext(EmojiLangParser.Table_insideContext,0)


        def getRuleIndex(self):
            return EmojiLangParser.RULE_table_inside

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_inside" ):
                listener.enterTable_inside(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_inside" ):
                listener.exitTable_inside(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_inside" ):
                return visitor.visitTable_inside(self)
            else:
                return visitor.visitChildren(self)




    def table_inside(self):

        localctx = EmojiLangParser.Table_insideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_table_inside)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.expr(0)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 63
                self.match(EmojiLangParser.COMMA)
                self.state = 64
                self.table_inside()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EmojiLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BoolTypeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bool_type(self):
            return self.getTypedRuleContext(EmojiLangParser.Bool_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolType" ):
                listener.enterBoolType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolType" ):
                listener.exitBoolType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolType" ):
                return visitor.visitBoolType(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(EmojiLangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EmojiLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(EmojiLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(EmojiLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(EmojiLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(EmojiLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogicExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bool_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EmojiLangParser.Bool_typeContext)
            else:
                return self.getTypedRuleContext(EmojiLangParser.Bool_typeContext,i)

        def AND(self):
            return self.getToken(EmojiLangParser.AND, 0)
        def OR(self):
            return self.getToken(EmojiLangParser.OR, 0)
        def XOR(self):
            return self.getToken(EmojiLangParser.XOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAccessExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(EmojiLangParser.ID, 0)
        def LBRACK(self):
            return self.getToken(EmojiLangParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(EmojiLangParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(EmojiLangParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccessExpr" ):
                listener.enterArrayAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccessExpr" ):
                listener.exitArrayAccessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccessExpr" ):
                return visitor.visitArrayAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEG(self):
            return self.getToken(EmojiLangParser.NEG, 0)
        def bool_type(self):
            return self.getTypedRuleContext(EmojiLangParser.Bool_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegExpr" ):
                listener.enterNegExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegExpr" ):
                listener.exitNegExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(EmojiLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(EmojiLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EmojiLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(EmojiLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(EmojiLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(EmojiLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EmojiLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = EmojiLangParser.LogicExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 68
                self.bool_type()
                self.state = 69
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.bool_type()
                pass

            elif la_ == 2:
                localctx = EmojiLangParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(EmojiLangParser.NEG)
                self.state = 73
                self.bool_type()
                pass

            elif la_ == 3:
                localctx = EmojiLangParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(EmojiLangParser.INT)
                pass

            elif la_ == 4:
                localctx = EmojiLangParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                self.match(EmojiLangParser.FLOAT)
                pass

            elif la_ == 5:
                localctx = EmojiLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(EmojiLangParser.ID)
                pass

            elif la_ == 6:
                localctx = EmojiLangParser.ArrayAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(EmojiLangParser.ID)
                self.state = 78
                self.match(EmojiLangParser.LBRACK)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.match(EmojiLangParser.RBRACK)
                pass

            elif la_ == 7:
                localctx = EmojiLangParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(EmojiLangParser.T__0)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(EmojiLangParser.T__1)
                pass

            elif la_ == 8:
                localctx = EmojiLangParser.BoolTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.bool_type()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 95
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = EmojiLangParser.MulDivExprContext(self, EmojiLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 90
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = EmojiLangParser.AddSubExprContext(self, EmojiLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 93
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 94
                        self.expr(10)
                        pass

             
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Bool_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EmojiLangParser.RULE_bool_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TrueExprContext(Bool_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.Bool_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(EmojiLangParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueExpr" ):
                listener.enterTrueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueExpr" ):
                listener.exitTrueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueExpr" ):
                return visitor.visitTrueExpr(self)
            else:
                return visitor.visitChildren(self)


    class FalseExprContext(Bool_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.Bool_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(EmojiLangParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseExpr" ):
                listener.enterFalseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseExpr" ):
                listener.exitFalseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseExpr" ):
                return visitor.visitFalseExpr(self)
            else:
                return visitor.visitChildren(self)



    def bool_type(self):

        localctx = EmojiLangParser.Bool_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bool_type)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = EmojiLangParser.TrueExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(EmojiLangParser.TRUE)
                pass
            elif token in [20]:
                localctx = EmojiLangParser.FalseExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(EmojiLangParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EmojiLangParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_TYPE(self):
            return self.getToken(EmojiLangParser.INT_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntType" ):
                listener.enterIntType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntType" ):
                listener.exitIntType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntType" ):
                return visitor.visitIntType(self)
            else:
                return visitor.visitChildren(self)


    class FloatTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EmojiLangParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_TYPE(self):
            return self.getToken(EmojiLangParser.FLOAT_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatType" ):
                listener.enterFloatType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatType" ):
                listener.exitFloatType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatType" ):
                return visitor.visitFloatType(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = EmojiLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = EmojiLangParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(EmojiLangParser.INT_TYPE)
                pass
            elif token in [4]:
                localctx = EmojiLangParser.FloatTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(EmojiLangParser.FLOAT_TYPE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         




