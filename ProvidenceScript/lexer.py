from tokens import Integer, Float, Operation, Declaration, Variable, Boolean, Comparison, Reserved

class Lexer:
    # Definitii sa functioneze
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-/*()="
    stopwords = [" "]
    declarations = ["make"]
    boolean = ["and", "or", "not"]
    comparisons = [">", "<", ">=", "<=", "?="]
    specialCharacters = "><=?"
    reserved = ["if", "elif", "else", "do", "while"]

    def __init__(self, text):
        # Initializeaza Lexer-u cu text pt tokenizare
        self.text = text
        self.idx = 0  # Index to track current character
        self.tokens = []  # List to store tokens
        self.char = self.text[self.idx]  # Current character
        self.token = None  # Current token being processed
    
    def tokenize(self):
        # Tokenizare input text
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                # Extract and classify numbers
                self.token = self.extract_number()
            
            elif self.char in Lexer.operations:
                # Handle basic operations like +, -, *, /, (, ), =
                self.token = Operation(self.char)
                self.move()
            
            elif self.char in Lexer.stopwords:
                # Skip whitespace/spacebar characters
                self.move()
                continue

            elif self.char in Lexer.letters:
                # Extract words (variables, keywords, declarations)
                word = self.extract_word()

                if word in Lexer.declarations:
                    self.token = Declaration(word)
                elif word in Lexer.boolean:
                    self.token = Boolean(word)
                elif word in Lexer.reserved:
                    self.token = Reserved(word)
                else:
                    self.token = Variable(word)
            
            elif self.char in Lexer.specialCharacters:
                # Handle comparison operators like >, <, >=, <=, ?=
                comparisonOperator = ""
                while self.char in Lexer.specialCharacters and self.idx < len(self.text):
                    comparisonOperator += self.char
                    self.move()
                
                self.token = Comparison(comparisonOperator)
            
            self.tokens.append(self.token)
        
        return self.tokens

    def extract_number(self):
        # "Extract numeric literals" scoate nr. literally (integers and floats)
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()
        
        return Integer(number) if not isFloat else Float(number)
    
    def extract_word(self):
        # Extract sequences of letters (words)
        word = ""
        while self.char in Lexer.letters and self.idx < len(self.text):
            word += self.char
            self.move()
        
        return word
    
    def move(self):
        # Move to the next character in the text
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]
