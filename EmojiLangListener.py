# Generated from EmojiLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EmojiLangParser import EmojiLangParser
else:
    from EmojiLangParser import EmojiLangParser

# This class defines a complete listener for a parse tree produced by EmojiLangParser.
class EmojiLangListener(ParseTreeListener):

    # Enter a parse tree produced by EmojiLangParser#program.
    def enterProgram(self, ctx:EmojiLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#program.
    def exitProgram(self, ctx:EmojiLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#PrintStmt.
    def enterPrintStmt(self, ctx:EmojiLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#PrintStmt.
    def exitPrintStmt(self, ctx:EmojiLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#AssignStmt.
    def enterAssignStmt(self, ctx:EmojiLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#AssignStmt.
    def exitAssignStmt(self, ctx:EmojiLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#FloatExpr.
    def enterFloatExpr(self, ctx:EmojiLangParser.FloatExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#FloatExpr.
    def exitFloatExpr(self, ctx:EmojiLangParser.FloatExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:EmojiLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:EmojiLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#IdExpr.
    def enterIdExpr(self, ctx:EmojiLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#IdExpr.
    def exitIdExpr(self, ctx:EmojiLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#IntExpr.
    def enterIntExpr(self, ctx:EmojiLangParser.IntExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#IntExpr.
    def exitIntExpr(self, ctx:EmojiLangParser.IntExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:EmojiLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:EmojiLangParser.AddSubExprContext):
        pass



del EmojiLangParser