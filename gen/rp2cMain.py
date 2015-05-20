from antlr4 import *
from rp2cLexer import rp2cLexer
from rp2cParser import rp2cParser

from rp2cListener import rp2cListener
import sys

#def main(argv):
def main():
    #sys.stderr = open("error.txt", "w")
    input = FileStream("input.txt")
    lexer = rp2cLexer(input)
    stream = CommonTokenStream(lexer)
    parser = rp2cParser(stream)
    tree = parser.program()
    walker = ParseTreeWalker()
    walker.walk(rp2cListener(), tree)

if __name__ == '__main__':
    #main(sys.argv)
    main()
