from antlr4 import *
from ChefScriptVisitor import ChefScriptVisitor
from ChefScriptParser import ChefScriptParser


class ChefScriptEvalVisitor(ChefScriptVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.return_value = None
        self.in_loop = False

    def visitProgram(self, ctx: ChefScriptParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitIngredientDeclaration(self, ctx: ChefScriptParser.IngredientDeclarationContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[name] = value

    def visitDishStatement(self, ctx: ChefScriptParser.DishStatementContext):
        value = self.visit(ctx.expression())
        print(value)

    def visitAssignmentStatement(self, ctx: ChefScriptParser.AssignmentStatementContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[name] = value

    def visitTasteStatement(self, ctx: ChefScriptParser.TasteStatementContext):
        if self.visit(ctx.expression()):
            self.visit(ctx.block(0))
            return
        for more_ctx in ctx.tasteMoreBlock():
            if self.visit(more_ctx.expression()):
                self.visit(more_ctx.block())
                return
        if ctx.ELSE():
            self.visit(ctx.block(len(ctx.block()) - 1))

    def visitFunctionDeclaration(self, ctx: ChefScriptParser.FunctionDeclarationContext):
        name = ctx.ID().getText()
        params = []
        if ctx.paramList():
            params = [p.ID().getText() for p in ctx.paramList().param()]
        self.functions[name] = (params, ctx.block())

    def visitFunctionCallStatement(self, ctx: ChefScriptParser.FunctionCallStatementContext):
        self.visit(ctx.functionCall())
        return None

    def visitFunctionCallExpr(self, ctx: ChefScriptParser.FunctionCallExprContext):
        return self.visit(ctx.functionCall())


    def visitFunctionCall(self, ctx: ChefScriptParser.FunctionCallContext):
        name = ctx.ID().getText()
        args = [self.visit(e) for e in ctx.argumentList().expression()] if ctx.argumentList() else []
        if name not in self.functions:
            line = ctx.start.line
            column = ctx.start.column
            raise RuntimeError(f"❌ Runtime error at line {line}, column {column}: Undefined function: {name}")
        params, body = self.functions[name]
        if len(params) != len(args):
            line = ctx.start.line
            column = ctx.start.column
            raise RuntimeError(f"❌ Runtime error at line {line}, column {column}: Function {name} expects {len(params)} args, got {len(args)}")
        old_vars = self.variables.copy()
        for p, a in zip(params, args):
            self.variables[p] = a
        try:
            self.visit(body)
        except ReturnFromFunction as ret:
            result = ret.value
        else:
            result = None
        self.variables = old_vars
        return result

    def visitServeStatement(self, ctx: ChefScriptParser.ServeStatementContext):
        value = self.visit(ctx.expression())
        self.return_value = value
        raise ReturnFromFunction(value)

    def visitStirStatement(self, ctx: ChefScriptParser.StirStatementContext):
        self.visit(ctx.ingredientDeclaration())
        cond = ctx.expression()
        update = ctx.assignmentStatement()
        block = ctx.block()
        self.in_loop = True
        while self.visit(cond):
            self.visit(block)
            self.visit(update)
        self.in_loop = False

    def visitMultiplyExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if isinstance(left, str) or isinstance(right, str):
            line = ctx.start.line
            column = ctx.start.column
            raise RuntimeError(f"❌ Runtime error at line {line}, column {column}: Cannot multiply string values")
        return left * right

    def visitDivideExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if right == 0:
            line = ctx.start.line
            column = ctx.start.column
            raise RuntimeError(f"❌ Runtime error at line {line}, column {column}: Division by zero")
        return left / right

    def visitAddExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if isinstance(left, str) or isinstance(right, str):
            return str(left) + str(right)
        return left + right

    def visitSubtractExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if isinstance(left, str) or isinstance(right, str):
            line = ctx.start.line
            column = ctx.start.column
            raise RuntimeError(f"❌ Runtime error at line {line}, column {column}: Cannot subtract string values")
        return left - right

    def visitGreaterExpr(self, ctx):
        return self.visit(ctx.expression(0)) > self.visit(ctx.expression(1))

    def visitLessExpr(self, ctx):
        return self.visit(ctx.expression(0)) < self.visit(ctx.expression(1))

    def visitGreaterEqualExpr(self, ctx):
        return self.visit(ctx.expression(0)) >= self.visit(ctx.expression(1))

    def visitLessEqualExpr(self, ctx):
        return self.visit(ctx.expression(0)) <= self.visit(ctx.expression(1))

    def visitSameExpr(self, ctx):
        return self.visit(ctx.expression(0)) == self.visit(ctx.expression(1))

    def visitNotSameExpr(self, ctx):
        return self.visit(ctx.expression(0)) != self.visit(ctx.expression(1))

    def visitAndExpr(self, ctx):
        return self.visit(ctx.expression(0)) and self.visit(ctx.expression(1))

    def visitOrExpr(self, ctx):
        return self.visit(ctx.expression(0)) or self.visit(ctx.expression(1))

    def visitNotExpr(self, ctx):
        return not self.visit(ctx.expression())


    def visitParensExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitNumberExpr(self, ctx):
        text = ctx.NUMBER().getText()
        return float(text) if '.' in text else int(text)

    def visitStringExpr(self, ctx):
        return ctx.STRING().getText().strip('"')

    def visitTrueExpr(self, ctx):
        return True

    def visitFalseExpr(self, ctx):
        return False

    def visitVariableExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.variables:
            line = ctx.start.line
            column = ctx.start.column
            raise RuntimeError(f"❌ Runtime error at line {line}, column {column}: Undefined variable: {name}")
        return self.variables[name]
    
    def visitBlock(self, ctx: ChefScriptParser.BlockContext):
        old_vars = self.variables.copy()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.variables = old_vars



class ReturnFromFunction(Exception):
    def __init__(self, value):
        self.value = value
