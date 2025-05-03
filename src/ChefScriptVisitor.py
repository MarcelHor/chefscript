# Generated from grammar/ChefScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChefScriptParser import ChefScriptParser
else:
    from ChefScriptParser import ChefScriptParser

# This class defines a complete generic visitor for a parse tree produced by ChefScriptParser.

class ChefScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ChefScriptParser#program.
    def visitProgram(self, ctx:ChefScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#statement.
    def visitStatement(self, ctx:ChefScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#ingredientDeclaration.
    def visitIngredientDeclaration(self, ctx:ChefScriptParser.IngredientDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#dishStatement.
    def visitDishStatement(self, ctx:ChefScriptParser.DishStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:ChefScriptParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#tasteStatement.
    def visitTasteStatement(self, ctx:ChefScriptParser.TasteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#tasteMoreBlock.
    def visitTasteMoreBlock(self, ctx:ChefScriptParser.TasteMoreBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:ChefScriptParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#functionCallStatement.
    def visitFunctionCallStatement(self, ctx:ChefScriptParser.FunctionCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#functionCall.
    def visitFunctionCall(self, ctx:ChefScriptParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#paramList.
    def visitParamList(self, ctx:ChefScriptParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#param.
    def visitParam(self, ctx:ChefScriptParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#argumentList.
    def visitArgumentList(self, ctx:ChefScriptParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#stirStatement.
    def visitStirStatement(self, ctx:ChefScriptParser.StirStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#serveStatement.
    def visitServeStatement(self, ctx:ChefScriptParser.ServeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#block.
    def visitBlock(self, ctx:ChefScriptParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#divideExpr.
    def visitDivideExpr(self, ctx:ChefScriptParser.DivideExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#subtractExpr.
    def visitSubtractExpr(self, ctx:ChefScriptParser.SubtractExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#notSameExpr.
    def visitNotSameExpr(self, ctx:ChefScriptParser.NotSameExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#trueExpr.
    def visitTrueExpr(self, ctx:ChefScriptParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#numberExpr.
    def visitNumberExpr(self, ctx:ChefScriptParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#lessExpr.
    def visitLessExpr(self, ctx:ChefScriptParser.LessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#orExpr.
    def visitOrExpr(self, ctx:ChefScriptParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#parensExpr.
    def visitParensExpr(self, ctx:ChefScriptParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#multiplyExpr.
    def visitMultiplyExpr(self, ctx:ChefScriptParser.MultiplyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#greaterEqualExpr.
    def visitGreaterEqualExpr(self, ctx:ChefScriptParser.GreaterEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#sameExpr.
    def visitSameExpr(self, ctx:ChefScriptParser.SameExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#stringExpr.
    def visitStringExpr(self, ctx:ChefScriptParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#lessEqualExpr.
    def visitLessEqualExpr(self, ctx:ChefScriptParser.LessEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#variableExpr.
    def visitVariableExpr(self, ctx:ChefScriptParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#greaterExpr.
    def visitGreaterExpr(self, ctx:ChefScriptParser.GreaterExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#notExpr.
    def visitNotExpr(self, ctx:ChefScriptParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#addExpr.
    def visitAddExpr(self, ctx:ChefScriptParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#functionCallExpr.
    def visitFunctionCallExpr(self, ctx:ChefScriptParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#falseExpr.
    def visitFalseExpr(self, ctx:ChefScriptParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ChefScriptParser#andExpr.
    def visitAndExpr(self, ctx:ChefScriptParser.AndExprContext):
        return self.visitChildren(ctx)



del ChefScriptParser