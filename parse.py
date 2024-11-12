import sys
from lex import *

class Parser:
    def __init__ (self, lexer):
        self.lexer = lexer
        
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
    
    def checkToken(self, kind):
        return kind == self.curToken.kind
    
    def checkPeek(self, kind):
        return kind == self.peekToken.kind
    
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name+ " ,got " + self.curToken.kind.name)
        self.nextToken()
    
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
    
    def abort(self, message):
        sys.exit("Erorr: " + message)
        
    def program(self):
        print("PROGRAM")
        
        while not self.checkToken(TokenType.EOF):
            self.statement()
            
    def statement(self):
        
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT_PRINT")
            self.nextToken()
            
            if self.checkToken(TokenType.STRING):
                self.nextToken()
            else:
                self.expression()
        
        elif self.checkToken(TokenType.IF):
            print("STATEMENT-IF")
            self.nextToken()
            self.comparison()
                
            self.match(TokenType.THEN)
            self.nl()
                
            while not self.checkToken(TokenType.ENDIF):
                self.statement()
            self.match(TokenType.ENDIF)        
        
        self.nl()
    
    def nl(self):
        print("NEWLINE")
        
        self.match(TokenType.NEWLINE)
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
        