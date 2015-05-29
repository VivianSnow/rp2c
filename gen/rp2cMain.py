from antlr4 import *
from rp2cLexer import rp2cLexer
from rp2cParser import rp2cParser

from rp2cListener import rp2cListener
import sys

def main(argv):
#def main():
    #sys.stderr = open("error.txt", "w")
    if len(argv) == 1:
        print u"you fu**ing idiot, please use -help to catch help info"
        return 
    elif len(argv) == 2 and argv[1] == "-help":
        print u"Use like this: rp2cMain.py source.pas dest.cpp"
        return
    elif len(argv) == 2:
        input = FileStream(argv[1].encode())
    elif len(argv) == 3:
        input = FileStream(argv[1].encode())
        sys.stdout = open(argv[2].encode(), "w")
    #input = FileStream("input.txt")
    lexer = rp2cLexer(input)
    stream = CommonTokenStream(lexer)
    parser = rp2cParser(stream)
    tree = parser.program()
    walker = ParseTreeWalker()
    walker.walk(rp2cListener(), tree)

if __name__ == '__main__':
    main(sys.argv)
    #main()
