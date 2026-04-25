import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from EmojiLangLexer import EmojiLangLexer
from EmojiLangParser import EmojiLangParser
from VisitorInterp import EmojiCompiler

class EmojiErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Błąd składniowy (Linia {line}, Kolumna {column}): {msg}", file=sys.stderr)
        sys.exit(1)

def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = EmojiLangLexer(input_stream)

    lexer.removeErrorListeners()
    lexer.addErrorListener(EmojiErrorListener())


    stream = CommonTokenStream(lexer)
    parser = EmojiLangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(EmojiErrorListener())

    tree = parser.program()
    try:
        vinterp = EmojiCompiler()
        vinterp.visit(tree)
    except Exception as e:
        print(f"{e}", file=sys.stderr)
        sys.exit(1)
    llvm_code = vinterp.finish()
    with open("wynik.ll", "w", encoding='utf-8') as f:
            f.write(llvm_code)

    print("ll file success")

if __name__ == '__main__':
    main(sys.argv)