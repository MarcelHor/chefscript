# Generated from grammar/ChefScript.g4 by ANTLR 4.13.2
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
        4,1,34,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,5,1,5,3,5,83,8,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,95,8,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,9,1,9,1,9,3,9,106,8,9,1,9,1,9,1,10,1,10,1,10,5,10,113,8,10,
        10,10,12,10,116,9,10,1,11,1,11,1,11,1,12,1,12,1,12,5,12,124,8,12,
        10,12,12,12,127,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,15,1,15,5,15,144,8,15,10,15,12,15,147,9,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,164,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,5,16,202,8,16,10,16,12,16,205,9,16,1,16,0,1,32,17,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,0,223,0,37,1,0,0,0,2,
        50,1,0,0,0,4,52,1,0,0,0,6,58,1,0,0,0,8,64,1,0,0,0,10,69,1,0,0,0,
        12,84,1,0,0,0,14,90,1,0,0,0,16,99,1,0,0,0,18,102,1,0,0,0,20,109,
        1,0,0,0,22,117,1,0,0,0,24,120,1,0,0,0,26,128,1,0,0,0,28,137,1,0,
        0,0,30,141,1,0,0,0,32,163,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,
        39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,
        0,40,41,5,0,0,1,41,1,1,0,0,0,42,51,3,4,2,0,43,51,3,6,3,0,44,51,3,
        8,4,0,45,51,3,10,5,0,46,51,3,14,7,0,47,51,3,16,8,0,48,51,3,26,13,
        0,49,51,3,28,14,0,50,42,1,0,0,0,50,43,1,0,0,0,50,44,1,0,0,0,50,45,
        1,0,0,0,50,46,1,0,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,
        51,3,1,0,0,0,52,53,5,21,0,0,53,54,5,31,0,0,54,55,5,1,0,0,55,56,3,
        32,16,0,56,57,5,2,0,0,57,5,1,0,0,0,58,59,5,22,0,0,59,60,5,3,0,0,
        60,61,3,32,16,0,61,62,5,4,0,0,62,63,5,2,0,0,63,7,1,0,0,0,64,65,5,
        31,0,0,65,66,5,1,0,0,66,67,3,32,16,0,67,68,5,2,0,0,68,9,1,0,0,0,
        69,70,5,23,0,0,70,71,5,3,0,0,71,72,3,32,16,0,72,73,5,4,0,0,73,77,
        3,30,15,0,74,76,3,12,6,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,
        0,77,78,1,0,0,0,78,82,1,0,0,0,79,77,1,0,0,0,80,81,5,25,0,0,81,83,
        3,30,15,0,82,80,1,0,0,0,82,83,1,0,0,0,83,11,1,0,0,0,84,85,5,24,0,
        0,85,86,5,3,0,0,86,87,3,32,16,0,87,88,5,4,0,0,88,89,3,30,15,0,89,
        13,1,0,0,0,90,91,5,26,0,0,91,92,5,31,0,0,92,94,5,3,0,0,93,95,3,20,
        10,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,5,4,0,0,97,
        98,3,30,15,0,98,15,1,0,0,0,99,100,3,18,9,0,100,101,5,2,0,0,101,17,
        1,0,0,0,102,103,5,31,0,0,103,105,5,3,0,0,104,106,3,24,12,0,105,104,
        1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,4,0,0,108,19,1,
        0,0,0,109,114,3,22,11,0,110,111,5,5,0,0,111,113,3,22,11,0,112,110,
        1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,21,1,
        0,0,0,116,114,1,0,0,0,117,118,5,21,0,0,118,119,5,31,0,0,119,23,1,
        0,0,0,120,125,3,32,16,0,121,122,5,5,0,0,122,124,3,32,16,0,123,121,
        1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,25,1,
        0,0,0,127,125,1,0,0,0,128,129,5,28,0,0,129,130,5,3,0,0,130,131,3,
        4,2,0,131,132,3,32,16,0,132,133,5,2,0,0,133,134,3,8,4,0,134,135,
        5,4,0,0,135,136,3,30,15,0,136,27,1,0,0,0,137,138,5,27,0,0,138,139,
        3,32,16,0,139,140,5,2,0,0,140,29,1,0,0,0,141,145,5,6,0,0,142,144,
        3,2,1,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,
        1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,5,7,0,0,149,31,1,
        0,0,0,150,151,6,16,-1,0,151,152,5,20,0,0,152,164,3,32,16,8,153,154,
        5,3,0,0,154,155,3,32,16,0,155,156,5,4,0,0,156,164,1,0,0,0,157,164,
        5,32,0,0,158,164,5,33,0,0,159,164,5,29,0,0,160,164,5,30,0,0,161,
        164,3,18,9,0,162,164,5,31,0,0,163,150,1,0,0,0,163,153,1,0,0,0,163,
        157,1,0,0,0,163,158,1,0,0,0,163,159,1,0,0,0,163,160,1,0,0,0,163,
        161,1,0,0,0,163,162,1,0,0,0,164,203,1,0,0,0,165,166,10,20,0,0,166,
        167,5,8,0,0,167,202,3,32,16,21,168,169,10,19,0,0,169,170,5,9,0,0,
        170,202,3,32,16,20,171,172,10,18,0,0,172,173,5,10,0,0,173,202,3,
        32,16,19,174,175,10,17,0,0,175,176,5,11,0,0,176,202,3,32,16,18,177,
        178,10,16,0,0,178,179,5,12,0,0,179,202,3,32,16,17,180,181,10,15,
        0,0,181,182,5,13,0,0,182,202,3,32,16,16,183,184,10,14,0,0,184,185,
        5,14,0,0,185,202,3,32,16,15,186,187,10,13,0,0,187,188,5,15,0,0,188,
        202,3,32,16,14,189,190,10,12,0,0,190,191,5,16,0,0,191,202,3,32,16,
        13,192,193,10,11,0,0,193,194,5,17,0,0,194,202,3,32,16,12,195,196,
        10,10,0,0,196,197,5,18,0,0,197,202,3,32,16,11,198,199,10,9,0,0,199,
        200,5,19,0,0,200,202,3,32,16,10,201,165,1,0,0,0,201,168,1,0,0,0,
        201,171,1,0,0,0,201,174,1,0,0,0,201,177,1,0,0,0,201,180,1,0,0,0,
        201,183,1,0,0,0,201,186,1,0,0,0,201,189,1,0,0,0,201,192,1,0,0,0,
        201,195,1,0,0,0,201,198,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,
        203,204,1,0,0,0,204,33,1,0,0,0,205,203,1,0,0,0,12,37,50,77,82,94,
        105,114,125,145,163,201,203
    ]

class ChefScriptParser ( Parser ):

    grammarFileName = "ChefScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'('", "')'", "','", "'{'", 
                     "'}'", "'*'", "'/'", "'+'", "'-'", "'>'", "'<'", "'>='", 
                     "'<='", "'same'", "'notSame'", "'mix'", "'either'", 
                     "'ew'", "'ingredient'", "'dish'", "'taste'", "'taste more'", 
                     "'else'", "'recipe'", "'serve'", "'stir'", "'true'", 
                     "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INGREDIENT", "DISH", "TASTE", "TASTE_MORE", 
                      "ELSE", "RECIPE", "SERVE", "STIR", "TRUE", "FALSE", 
                      "ID", "NUMBER", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_ingredientDeclaration = 2
    RULE_dishStatement = 3
    RULE_assignmentStatement = 4
    RULE_tasteStatement = 5
    RULE_tasteMoreBlock = 6
    RULE_functionDeclaration = 7
    RULE_functionCallStatement = 8
    RULE_functionCall = 9
    RULE_paramList = 10
    RULE_param = 11
    RULE_argumentList = 12
    RULE_stirStatement = 13
    RULE_serveStatement = 14
    RULE_block = 15
    RULE_expression = 16

    ruleNames =  [ "program", "statement", "ingredientDeclaration", "dishStatement", 
                   "assignmentStatement", "tasteStatement", "tasteMoreBlock", 
                   "functionDeclaration", "functionCallStatement", "functionCall", 
                   "paramList", "param", "argumentList", "stirStatement", 
                   "serveStatement", "block", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    INGREDIENT=21
    DISH=22
    TASTE=23
    TASTE_MORE=24
    ELSE=25
    RECIPE=26
    SERVE=27
    STIR=28
    TRUE=29
    FALSE=30
    ID=31
    NUMBER=32
    STRING=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ChefScriptParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_program

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

        localctx = ChefScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2631925760) != 0):
                self.state = 34
                self.statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(ChefScriptParser.EOF)
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

        def ingredientDeclaration(self):
            return self.getTypedRuleContext(ChefScriptParser.IngredientDeclarationContext,0)


        def dishStatement(self):
            return self.getTypedRuleContext(ChefScriptParser.DishStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(ChefScriptParser.AssignmentStatementContext,0)


        def tasteStatement(self):
            return self.getTypedRuleContext(ChefScriptParser.TasteStatementContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(ChefScriptParser.FunctionDeclarationContext,0)


        def functionCallStatement(self):
            return self.getTypedRuleContext(ChefScriptParser.FunctionCallStatementContext,0)


        def stirStatement(self):
            return self.getTypedRuleContext(ChefScriptParser.StirStatementContext,0)


        def serveStatement(self):
            return self.getTypedRuleContext(ChefScriptParser.ServeStatementContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ChefScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.ingredientDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.dishStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.assignmentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.tasteStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.functionDeclaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.functionCallStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 48
                self.stirStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 49
                self.serveStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IngredientDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INGREDIENT(self):
            return self.getToken(ChefScriptParser.INGREDIENT, 0)

        def ID(self):
            return self.getToken(ChefScriptParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_ingredientDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIngredientDeclaration" ):
                listener.enterIngredientDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIngredientDeclaration" ):
                listener.exitIngredientDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIngredientDeclaration" ):
                return visitor.visitIngredientDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def ingredientDeclaration(self):

        localctx = ChefScriptParser.IngredientDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ingredientDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ChefScriptParser.INGREDIENT)
            self.state = 53
            self.match(ChefScriptParser.ID)
            self.state = 54
            self.match(ChefScriptParser.T__0)
            self.state = 55
            self.expression(0)
            self.state = 56
            self.match(ChefScriptParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DishStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISH(self):
            return self.getToken(ChefScriptParser.DISH, 0)

        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_dishStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDishStatement" ):
                listener.enterDishStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDishStatement" ):
                listener.exitDishStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDishStatement" ):
                return visitor.visitDishStatement(self)
            else:
                return visitor.visitChildren(self)




    def dishStatement(self):

        localctx = ChefScriptParser.DishStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dishStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ChefScriptParser.DISH)
            self.state = 59
            self.match(ChefScriptParser.T__2)
            self.state = 60
            self.expression(0)
            self.state = 61
            self.match(ChefScriptParser.T__3)
            self.state = 62
            self.match(ChefScriptParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ChefScriptParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = ChefScriptParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ChefScriptParser.ID)
            self.state = 65
            self.match(ChefScriptParser.T__0)
            self.state = 66
            self.expression(0)
            self.state = 67
            self.match(ChefScriptParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TasteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TASTE(self):
            return self.getToken(ChefScriptParser.TASTE, 0)

        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.BlockContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.BlockContext,i)


        def tasteMoreBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.TasteMoreBlockContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.TasteMoreBlockContext,i)


        def ELSE(self):
            return self.getToken(ChefScriptParser.ELSE, 0)

        def getRuleIndex(self):
            return ChefScriptParser.RULE_tasteStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTasteStatement" ):
                listener.enterTasteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTasteStatement" ):
                listener.exitTasteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTasteStatement" ):
                return visitor.visitTasteStatement(self)
            else:
                return visitor.visitChildren(self)




    def tasteStatement(self):

        localctx = ChefScriptParser.TasteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tasteStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ChefScriptParser.TASTE)
            self.state = 70
            self.match(ChefScriptParser.T__2)
            self.state = 71
            self.expression(0)
            self.state = 72
            self.match(ChefScriptParser.T__3)
            self.state = 73
            self.block()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 74
                self.tasteMoreBlock()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 80
                self.match(ChefScriptParser.ELSE)
                self.state = 81
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TasteMoreBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TASTE_MORE(self):
            return self.getToken(ChefScriptParser.TASTE_MORE, 0)

        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(ChefScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_tasteMoreBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTasteMoreBlock" ):
                listener.enterTasteMoreBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTasteMoreBlock" ):
                listener.exitTasteMoreBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTasteMoreBlock" ):
                return visitor.visitTasteMoreBlock(self)
            else:
                return visitor.visitChildren(self)




    def tasteMoreBlock(self):

        localctx = ChefScriptParser.TasteMoreBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tasteMoreBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ChefScriptParser.TASTE_MORE)
            self.state = 85
            self.match(ChefScriptParser.T__2)
            self.state = 86
            self.expression(0)
            self.state = 87
            self.match(ChefScriptParser.T__3)
            self.state = 88
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECIPE(self):
            return self.getToken(ChefScriptParser.RECIPE, 0)

        def ID(self):
            return self.getToken(ChefScriptParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(ChefScriptParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(ChefScriptParser.ParamListContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = ChefScriptParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(ChefScriptParser.RECIPE)
            self.state = 91
            self.match(ChefScriptParser.ID)
            self.state = 92
            self.match(ChefScriptParser.T__2)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 93
                self.paramList()


            self.state = 96
            self.match(ChefScriptParser.T__3)
            self.state = 97
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(ChefScriptParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_functionCallStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallStatement" ):
                listener.enterFunctionCallStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallStatement" ):
                listener.exitFunctionCallStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallStatement" ):
                return visitor.visitFunctionCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionCallStatement(self):

        localctx = ChefScriptParser.FunctionCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCallStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.functionCall()
            self.state = 100
            self.match(ChefScriptParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ChefScriptParser.ID, 0)

        def argumentList(self):
            return self.getTypedRuleContext(ChefScriptParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = ChefScriptParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ChefScriptParser.ID)
            self.state = 103
            self.match(ChefScriptParser.T__2)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16644046856) != 0):
                self.state = 104
                self.argumentList()


            self.state = 107
            self.match(ChefScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ParamContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ParamContext,i)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = ChefScriptParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.param()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 110
                self.match(ChefScriptParser.T__4)
                self.state = 111
                self.param()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INGREDIENT(self):
            return self.getToken(ChefScriptParser.INGREDIENT, 0)

        def ID(self):
            return self.getToken(ChefScriptParser.ID, 0)

        def getRuleIndex(self):
            return ChefScriptParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ChefScriptParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ChefScriptParser.INGREDIENT)
            self.state = 118
            self.match(ChefScriptParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = ChefScriptParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.expression(0)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 121
                self.match(ChefScriptParser.T__4)
                self.state = 122
                self.expression(0)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StirStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STIR(self):
            return self.getToken(ChefScriptParser.STIR, 0)

        def ingredientDeclaration(self):
            return self.getTypedRuleContext(ChefScriptParser.IngredientDeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(ChefScriptParser.AssignmentStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(ChefScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_stirStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStirStatement" ):
                listener.enterStirStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStirStatement" ):
                listener.exitStirStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStirStatement" ):
                return visitor.visitStirStatement(self)
            else:
                return visitor.visitChildren(self)




    def stirStatement(self):

        localctx = ChefScriptParser.StirStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stirStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(ChefScriptParser.STIR)
            self.state = 129
            self.match(ChefScriptParser.T__2)
            self.state = 130
            self.ingredientDeclaration()
            self.state = 131
            self.expression(0)
            self.state = 132
            self.match(ChefScriptParser.T__1)
            self.state = 133
            self.assignmentStatement()
            self.state = 134
            self.match(ChefScriptParser.T__3)
            self.state = 135
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERVE(self):
            return self.getToken(ChefScriptParser.SERVE, 0)

        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_serveStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServeStatement" ):
                listener.enterServeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServeStatement" ):
                listener.exitServeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitServeStatement" ):
                return visitor.visitServeStatement(self)
            else:
                return visitor.visitChildren(self)




    def serveStatement(self):

        localctx = ChefScriptParser.ServeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_serveStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ChefScriptParser.SERVE)
            self.state = 138
            self.expression(0)
            self.state = 139
            self.match(ChefScriptParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return ChefScriptParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ChefScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ChefScriptParser.T__5)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2631925760) != 0):
                self.state = 142
                self.statement()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.match(ChefScriptParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ChefScriptParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivideExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivideExpr" ):
                listener.enterDivideExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivideExpr" ):
                listener.exitDivideExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivideExpr" ):
                return visitor.visitDivideExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubtractExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtractExpr" ):
                listener.enterSubtractExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtractExpr" ):
                listener.exitSubtractExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtractExpr" ):
                return visitor.visitSubtractExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotSameExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotSameExpr" ):
                listener.enterNotSameExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotSameExpr" ):
                listener.exitNotSameExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotSameExpr" ):
                return visitor.visitNotSameExpr(self)
            else:
                return visitor.visitChildren(self)


    class TrueExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(ChefScriptParser.TRUE, 0)

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


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ChefScriptParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class LessExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessExpr" ):
                listener.enterLessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessExpr" ):
                listener.exitLessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessExpr" ):
                return visitor.visitLessExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


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


    class MultiplyExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyExpr" ):
                listener.enterMultiplyExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyExpr" ):
                listener.exitMultiplyExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplyExpr" ):
                return visitor.visitMultiplyExpr(self)
            else:
                return visitor.visitChildren(self)


    class GreaterEqualExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEqualExpr" ):
                listener.enterGreaterEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEqualExpr" ):
                listener.exitGreaterEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterEqualExpr" ):
                return visitor.visitGreaterEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class SameExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSameExpr" ):
                listener.enterSameExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSameExpr" ):
                listener.exitSameExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSameExpr" ):
                return visitor.visitSameExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ChefScriptParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class LessEqualExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessEqualExpr" ):
                listener.enterLessEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessEqualExpr" ):
                listener.exitLessEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessEqualExpr" ):
                return visitor.visitLessEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ChefScriptParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class GreaterExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterExpr" ):
                listener.enterGreaterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterExpr" ):
                listener.exitGreaterExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterExpr" ):
                return visitor.visitGreaterExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(ChefScriptParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class FalseExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(ChefScriptParser.FALSE, 0)

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


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ChefScriptParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChefScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ChefScriptParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ChefScriptParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = ChefScriptParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 151
                self.match(ChefScriptParser.T__19)
                self.state = 152
                self.expression(8)
                pass

            elif la_ == 2:
                localctx = ChefScriptParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(ChefScriptParser.T__2)
                self.state = 154
                self.expression(0)
                self.state = 155
                self.match(ChefScriptParser.T__3)
                pass

            elif la_ == 3:
                localctx = ChefScriptParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(ChefScriptParser.NUMBER)
                pass

            elif la_ == 4:
                localctx = ChefScriptParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(ChefScriptParser.STRING)
                pass

            elif la_ == 5:
                localctx = ChefScriptParser.TrueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(ChefScriptParser.TRUE)
                pass

            elif la_ == 6:
                localctx = ChefScriptParser.FalseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.match(ChefScriptParser.FALSE)
                pass

            elif la_ == 7:
                localctx = ChefScriptParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.functionCall()
                pass

            elif la_ == 8:
                localctx = ChefScriptParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(ChefScriptParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 201
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = ChefScriptParser.MultiplyExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 165
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 166
                        self.match(ChefScriptParser.T__7)
                        self.state = 167
                        self.expression(21)
                        pass

                    elif la_ == 2:
                        localctx = ChefScriptParser.DivideExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 169
                        self.match(ChefScriptParser.T__8)
                        self.state = 170
                        self.expression(20)
                        pass

                    elif la_ == 3:
                        localctx = ChefScriptParser.AddExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 171
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 172
                        self.match(ChefScriptParser.T__9)
                        self.state = 173
                        self.expression(19)
                        pass

                    elif la_ == 4:
                        localctx = ChefScriptParser.SubtractExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 174
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 175
                        self.match(ChefScriptParser.T__10)
                        self.state = 176
                        self.expression(18)
                        pass

                    elif la_ == 5:
                        localctx = ChefScriptParser.GreaterExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 177
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 178
                        self.match(ChefScriptParser.T__11)
                        self.state = 179
                        self.expression(17)
                        pass

                    elif la_ == 6:
                        localctx = ChefScriptParser.LessExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 180
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 181
                        self.match(ChefScriptParser.T__12)
                        self.state = 182
                        self.expression(16)
                        pass

                    elif la_ == 7:
                        localctx = ChefScriptParser.GreaterEqualExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 183
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 184
                        self.match(ChefScriptParser.T__13)
                        self.state = 185
                        self.expression(15)
                        pass

                    elif la_ == 8:
                        localctx = ChefScriptParser.LessEqualExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 187
                        self.match(ChefScriptParser.T__14)
                        self.state = 188
                        self.expression(14)
                        pass

                    elif la_ == 9:
                        localctx = ChefScriptParser.SameExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 190
                        self.match(ChefScriptParser.T__15)
                        self.state = 191
                        self.expression(13)
                        pass

                    elif la_ == 10:
                        localctx = ChefScriptParser.NotSameExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 193
                        self.match(ChefScriptParser.T__16)
                        self.state = 194
                        self.expression(12)
                        pass

                    elif la_ == 11:
                        localctx = ChefScriptParser.AndExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 196
                        self.match(ChefScriptParser.T__17)
                        self.state = 197
                        self.expression(11)
                        pass

                    elif la_ == 12:
                        localctx = ChefScriptParser.OrExprContext(self, ChefScriptParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 199
                        self.match(ChefScriptParser.T__18)
                        self.state = 200
                        self.expression(10)
                        pass

             
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 9)
         




