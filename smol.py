from lex import *

def main():
    source = "LET FOOTBAR = 123"
    lexer  = Lexer(source)
    
    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()
        
main()
        