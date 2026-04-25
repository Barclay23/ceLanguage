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


    # Enter a parse tree produced by EmojiLangParser#ReadStmt.
    def enterReadStmt(self, ctx:EmojiLangParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#ReadStmt.
    def exitReadStmt(self, ctx:EmojiLangParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#VarDeclStmt.
    def enterVarDeclStmt(self, ctx:EmojiLangParser.VarDeclStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#VarDeclStmt.
    def exitVarDeclStmt(self, ctx:EmojiLangParser.VarDeclStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#ArrayDeclStmt.
    def enterArrayDeclStmt(self, ctx:EmojiLangParser.ArrayDeclStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#ArrayDeclStmt.
    def exitArrayDeclStmt(self, ctx:EmojiLangParser.ArrayDeclStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#AssignStmt.
    def enterAssignStmt(self, ctx:EmojiLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#AssignStmt.
    def exitAssignStmt(self, ctx:EmojiLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#ArrayAssignStmt.
    def enterArrayAssignStmt(self, ctx:EmojiLangParser.ArrayAssignStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#ArrayAssignStmt.
    def exitArrayAssignStmt(self, ctx:EmojiLangParser.ArrayAssignStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#ArrayCellAssignStmt.
    def enterArrayCellAssignStmt(self, ctx:EmojiLangParser.ArrayCellAssignStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#ArrayCellAssignStmt.
    def exitArrayCellAssignStmt(self, ctx:EmojiLangParser.ArrayCellAssignStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#IfElseStmt.
    def enterIfElseStmt(self, ctx:EmojiLangParser.IfElseStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#IfElseStmt.
    def exitIfElseStmt(self, ctx:EmojiLangParser.IfElseStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#WhileStmt.
    def enterWhileStmt(self, ctx:EmojiLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#WhileStmt.
    def exitWhileStmt(self, ctx:EmojiLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#ReturnStmt.
    def enterReturnStmt(self, ctx:EmojiLangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#ReturnStmt.
    def exitReturnStmt(self, ctx:EmojiLangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#table_inside.
    def enterTable_inside(self, ctx:EmojiLangParser.Table_insideContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#table_inside.
    def exitTable_inside(self, ctx:EmojiLangParser.Table_insideContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#FloatExpr.
    def enterFloatExpr(self, ctx:EmojiLangParser.FloatExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#FloatExpr.
    def exitFloatExpr(self, ctx:EmojiLangParser.FloatExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#TrueExpr.
    def enterTrueExpr(self, ctx:EmojiLangParser.TrueExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#TrueExpr.
    def exitTrueExpr(self, ctx:EmojiLangParser.TrueExprContext):
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


    # Enter a parse tree produced by EmojiLangParser#LogicExpr.
    def enterLogicExpr(self, ctx:EmojiLangParser.LogicExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#LogicExpr.
    def exitLogicExpr(self, ctx:EmojiLangParser.LogicExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#ArrayAccessExpr.
    def enterArrayAccessExpr(self, ctx:EmojiLangParser.ArrayAccessExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#ArrayAccessExpr.
    def exitArrayAccessExpr(self, ctx:EmojiLangParser.ArrayAccessExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#NegExpr.
    def enterNegExpr(self, ctx:EmojiLangParser.NegExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#NegExpr.
    def exitNegExpr(self, ctx:EmojiLangParser.NegExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#ParensExpr.
    def enterParensExpr(self, ctx:EmojiLangParser.ParensExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#ParensExpr.
    def exitParensExpr(self, ctx:EmojiLangParser.ParensExprContext):
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


    # Enter a parse tree produced by EmojiLangParser#FalseExpr.
    def enterFalseExpr(self, ctx:EmojiLangParser.FalseExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#FalseExpr.
    def exitFalseExpr(self, ctx:EmojiLangParser.FalseExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:EmojiLangParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:EmojiLangParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#compare.
    def enterCompare(self, ctx:EmojiLangParser.CompareContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#compare.
    def exitCompare(self, ctx:EmojiLangParser.CompareContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#BoolValueExpr.
    def enterBoolValueExpr(self, ctx:EmojiLangParser.BoolValueExprContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#BoolValueExpr.
    def exitBoolValueExpr(self, ctx:EmojiLangParser.BoolValueExprContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#BlockLabel.
    def enterBlockLabel(self, ctx:EmojiLangParser.BlockLabelContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#BlockLabel.
    def exitBlockLabel(self, ctx:EmojiLangParser.BlockLabelContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#functionHeader.
    def enterFunctionHeader(self, ctx:EmojiLangParser.FunctionHeaderContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#functionHeader.
    def exitFunctionHeader(self, ctx:EmojiLangParser.FunctionHeaderContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#idList.
    def enterIdList(self, ctx:EmojiLangParser.IdListContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#idList.
    def exitIdList(self, ctx:EmojiLangParser.IdListContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#argumentList.
    def enterArgumentList(self, ctx:EmojiLangParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#argumentList.
    def exitArgumentList(self, ctx:EmojiLangParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#IntType.
    def enterIntType(self, ctx:EmojiLangParser.IntTypeContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#IntType.
    def exitIntType(self, ctx:EmojiLangParser.IntTypeContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#FloatType.
    def enterFloatType(self, ctx:EmojiLangParser.FloatTypeContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#FloatType.
    def exitFloatType(self, ctx:EmojiLangParser.FloatTypeContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#BoolTypeDecl.
    def enterBoolTypeDecl(self, ctx:EmojiLangParser.BoolTypeDeclContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#BoolTypeDecl.
    def exitBoolTypeDecl(self, ctx:EmojiLangParser.BoolTypeDeclContext):
        pass


    # Enter a parse tree produced by EmojiLangParser#scopeSpecifier.
    def enterScopeSpecifier(self, ctx:EmojiLangParser.ScopeSpecifierContext):
        pass

    # Exit a parse tree produced by EmojiLangParser#scopeSpecifier.
    def exitScopeSpecifier(self, ctx:EmojiLangParser.ScopeSpecifierContext):
        pass



del EmojiLangParser