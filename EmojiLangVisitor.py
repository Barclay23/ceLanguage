# Generated from EmojiLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EmojiLangParser import EmojiLangParser
else:
    from EmojiLangParser import EmojiLangParser

# This class defines a complete generic visitor for a parse tree produced by EmojiLangParser.

class EmojiLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EmojiLangParser#program.
    def visitProgram(self, ctx:EmojiLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#PrintStmt.
    def visitPrintStmt(self, ctx:EmojiLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#ReadStmt.
    def visitReadStmt(self, ctx:EmojiLangParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#VarDeclStmt.
    def visitVarDeclStmt(self, ctx:EmojiLangParser.VarDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#ArrayDeclStmt.
    def visitArrayDeclStmt(self, ctx:EmojiLangParser.ArrayDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#AssignStmt.
    def visitAssignStmt(self, ctx:EmojiLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#ArrayAssignStmt.
    def visitArrayAssignStmt(self, ctx:EmojiLangParser.ArrayAssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#ArrayCellAssignStmt.
    def visitArrayCellAssignStmt(self, ctx:EmojiLangParser.ArrayCellAssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#table_inside.
    def visitTable_inside(self, ctx:EmojiLangParser.Table_insideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#FloatExpr.
    def visitFloatExpr(self, ctx:EmojiLangParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#TrueExpr.
    def visitTrueExpr(self, ctx:EmojiLangParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:EmojiLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#IdExpr.
    def visitIdExpr(self, ctx:EmojiLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#LogicExpr.
    def visitLogicExpr(self, ctx:EmojiLangParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#ArrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:EmojiLangParser.ArrayAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#NegExpr.
    def visitNegExpr(self, ctx:EmojiLangParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#ParensExpr.
    def visitParensExpr(self, ctx:EmojiLangParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#IntExpr.
    def visitIntExpr(self, ctx:EmojiLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:EmojiLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#FalseExpr.
    def visitFalseExpr(self, ctx:EmojiLangParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#IntType.
    def visitIntType(self, ctx:EmojiLangParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#FloatType.
    def visitFloatType(self, ctx:EmojiLangParser.FloatTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmojiLangParser#BoolTypeDecl.
    def visitBoolTypeDecl(self, ctx:EmojiLangParser.BoolTypeDeclContext):
        return self.visitChildren(ctx)



del EmojiLangParser