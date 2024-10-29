from lex import *

def main():
    source = "+- */ >>= = #THis is a comment which is gonna get skipped \n !="
    lexer  = Lexer(source)
    
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()
        
main()