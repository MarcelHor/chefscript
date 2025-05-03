from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class ChefScriptErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseCancellationException(f"❌ Syntax error at line {line}, column {column}: {msg}")


    def getErrors(self):
        return self.errors
    