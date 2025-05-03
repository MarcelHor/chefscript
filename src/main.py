from antlr4 import *
from antlr4.error.Errors import ParseCancellationException
from ChefScriptLexer import ChefScriptLexer
from ChefScriptParser import ChefScriptParser
from ChefScriptEvalVisitor import ChefScriptEvalVisitor
from ChefScriptErrorListener import ChefScriptErrorListener
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("❌ Chybí název souboru. Použití: python3 main.py <soubor.chef>")
        return
    file_name = sys.argv[1]

    if not os.path.exists(file_name):
        print(f"❌ Soubor '{file_name}' neexistuje.")
        return
    
    try:
        input_stream = FileStream(file_name, encoding="utf=8")

        lexer = ChefScriptLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(ChefScriptErrorListener())

        stream = CommonTokenStream(lexer)

        parser = ChefScriptParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ChefScriptErrorListener())

        tree = parser.program()

        visitor = ChefScriptEvalVisitor()
        visitor.visit(tree)

    except ParseCancellationException as e:
        print(e)
    except RuntimeError as e:
        print(e)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
