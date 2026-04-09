import sys
from antlr4 import *
from EmojiLangLexer import EmojiLangLexer
from EmojiLangParser import EmojiLangParser
from VisitorInterp import MyEmojiCompiler

def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = EmojiLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = EmojiLangParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
        sys.exit(1)
    else:
        vinterp = MyEmojiCompiler()
        vinterp.visit(tree)

    llvm_code = vinterp.finish()
    with open("wynik.ll", "w", encoding='utf-8') as f:
            f.write(llvm_code)

    print("ll file success")

if __name__ == '__main__':
    main(sys.argv)