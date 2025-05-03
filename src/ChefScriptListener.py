# Generated from grammar/ChefScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChefScriptParser import ChefScriptParser
else:
    from ChefScriptParser import ChefScriptParser

# This class defines a complete listener for a parse tree produced by ChefScriptParser.
class ChefScriptListener(ParseTreeListener):

    # Enter a parse tree produced by ChefScriptParser#program.
    def enterProgram(self, ctx:ChefScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#program.
    def exitProgram(self, ctx:ChefScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#statement.
    def enterStatement(self, ctx:ChefScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#statement.
    def exitStatement(self, ctx:ChefScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#ingredientDeclaration.
    def enterIngredientDeclaration(self, ctx:ChefScriptParser.IngredientDeclarationContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#ingredientDeclaration.
    def exitIngredientDeclaration(self, ctx:ChefScriptParser.IngredientDeclarationContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#dishStatement.
    def enterDishStatement(self, ctx:ChefScriptParser.DishStatementContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#dishStatement.
    def exitDishStatement(self, ctx:ChefScriptParser.DishStatementContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:ChefScriptParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:ChefScriptParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#tasteStatement.
    def enterTasteStatement(self, ctx:ChefScriptParser.TasteStatementContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#tasteStatement.
    def exitTasteStatement(self, ctx:ChefScriptParser.TasteStatementContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#tasteMoreBlock.
    def enterTasteMoreBlock(self, ctx:ChefScriptParser.TasteMoreBlockContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#tasteMoreBlock.
    def exitTasteMoreBlock(self, ctx:ChefScriptParser.TasteMoreBlockContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:ChefScriptParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:ChefScriptParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#functionCallStatement.
    def enterFunctionCallStatement(self, ctx:ChefScriptParser.FunctionCallStatementContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#functionCallStatement.
    def exitFunctionCallStatement(self, ctx:ChefScriptParser.FunctionCallStatementContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#functionCall.
    def enterFunctionCall(self, ctx:ChefScriptParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#functionCall.
    def exitFunctionCall(self, ctx:ChefScriptParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#paramList.
    def enterParamList(self, ctx:ChefScriptParser.ParamListContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#paramList.
    def exitParamList(self, ctx:ChefScriptParser.ParamListContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#param.
    def enterParam(self, ctx:ChefScriptParser.ParamContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#param.
    def exitParam(self, ctx:ChefScriptParser.ParamContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#argumentList.
    def enterArgumentList(self, ctx:ChefScriptParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#argumentList.
    def exitArgumentList(self, ctx:ChefScriptParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#stirStatement.
    def enterStirStatement(self, ctx:ChefScriptParser.StirStatementContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#stirStatement.
    def exitStirStatement(self, ctx:ChefScriptParser.StirStatementContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#serveStatement.
    def enterServeStatement(self, ctx:ChefScriptParser.ServeStatementContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#serveStatement.
    def exitServeStatement(self, ctx:ChefScriptParser.ServeStatementContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#block.
    def enterBlock(self, ctx:ChefScriptParser.BlockContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#block.
    def exitBlock(self, ctx:ChefScriptParser.BlockContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#divideExpr.
    def enterDivideExpr(self, ctx:ChefScriptParser.DivideExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#divideExpr.
    def exitDivideExpr(self, ctx:ChefScriptParser.DivideExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#subtractExpr.
    def enterSubtractExpr(self, ctx:ChefScriptParser.SubtractExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#subtractExpr.
    def exitSubtractExpr(self, ctx:ChefScriptParser.SubtractExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#notSameExpr.
    def enterNotSameExpr(self, ctx:ChefScriptParser.NotSameExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#notSameExpr.
    def exitNotSameExpr(self, ctx:ChefScriptParser.NotSameExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#trueExpr.
    def enterTrueExpr(self, ctx:ChefScriptParser.TrueExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#trueExpr.
    def exitTrueExpr(self, ctx:ChefScriptParser.TrueExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#numberExpr.
    def enterNumberExpr(self, ctx:ChefScriptParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#numberExpr.
    def exitNumberExpr(self, ctx:ChefScriptParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#lessExpr.
    def enterLessExpr(self, ctx:ChefScriptParser.LessExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#lessExpr.
    def exitLessExpr(self, ctx:ChefScriptParser.LessExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#orExpr.
    def enterOrExpr(self, ctx:ChefScriptParser.OrExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#orExpr.
    def exitOrExpr(self, ctx:ChefScriptParser.OrExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#parensExpr.
    def enterParensExpr(self, ctx:ChefScriptParser.ParensExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#parensExpr.
    def exitParensExpr(self, ctx:ChefScriptParser.ParensExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#multiplyExpr.
    def enterMultiplyExpr(self, ctx:ChefScriptParser.MultiplyExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#multiplyExpr.
    def exitMultiplyExpr(self, ctx:ChefScriptParser.MultiplyExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#greaterEqualExpr.
    def enterGreaterEqualExpr(self, ctx:ChefScriptParser.GreaterEqualExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#greaterEqualExpr.
    def exitGreaterEqualExpr(self, ctx:ChefScriptParser.GreaterEqualExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#sameExpr.
    def enterSameExpr(self, ctx:ChefScriptParser.SameExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#sameExpr.
    def exitSameExpr(self, ctx:ChefScriptParser.SameExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#stringExpr.
    def enterStringExpr(self, ctx:ChefScriptParser.StringExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#stringExpr.
    def exitStringExpr(self, ctx:ChefScriptParser.StringExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#lessEqualExpr.
    def enterLessEqualExpr(self, ctx:ChefScriptParser.LessEqualExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#lessEqualExpr.
    def exitLessEqualExpr(self, ctx:ChefScriptParser.LessEqualExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#variableExpr.
    def enterVariableExpr(self, ctx:ChefScriptParser.VariableExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#variableExpr.
    def exitVariableExpr(self, ctx:ChefScriptParser.VariableExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#greaterExpr.
    def enterGreaterExpr(self, ctx:ChefScriptParser.GreaterExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#greaterExpr.
    def exitGreaterExpr(self, ctx:ChefScriptParser.GreaterExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#notExpr.
    def enterNotExpr(self, ctx:ChefScriptParser.NotExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#notExpr.
    def exitNotExpr(self, ctx:ChefScriptParser.NotExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#addExpr.
    def enterAddExpr(self, ctx:ChefScriptParser.AddExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#addExpr.
    def exitAddExpr(self, ctx:ChefScriptParser.AddExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#functionCallExpr.
    def enterFunctionCallExpr(self, ctx:ChefScriptParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#functionCallExpr.
    def exitFunctionCallExpr(self, ctx:ChefScriptParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#falseExpr.
    def enterFalseExpr(self, ctx:ChefScriptParser.FalseExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#falseExpr.
    def exitFalseExpr(self, ctx:ChefScriptParser.FalseExprContext):
        pass


    # Enter a parse tree produced by ChefScriptParser#andExpr.
    def enterAndExpr(self, ctx:ChefScriptParser.AndExprContext):
        pass

    # Exit a parse tree produced by ChefScriptParser#andExpr.
    def exitAndExpr(self, ctx:ChefScriptParser.AndExprContext):
        pass



del ChefScriptParser