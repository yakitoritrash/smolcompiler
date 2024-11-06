from lex import *
from parse import *
import sys

def main():
    
    print ("Smol Compiler")
    
    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()
        
    lexer  = Lexer(source)
    parser = Parser(lexer)
    
    parser.program()
    print("Parsing completed.")
        
main()