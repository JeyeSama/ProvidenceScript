class Token:
    def __init__(self, type, value):
        # Clasa de baza pentru toate tokenurile, tip si valoare
        self.type = type  # Tipul tokenului, de exemplu 'INT', 'OP', 'VAR', etc.
        self.value = value  # Valoarea tokenului, de exemplu 5 sau '+'

    def __repr__(self):
        # Reprezentarea tokenului, valoarea acestuia basically
        return str(self.value)

class Integer(Token):
    def __init__(self, value):
        # Token pentru numere intregi, tipul va fi 'INT'
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        # Token pentru numere cu virgula mobila (floating point), tipul va fi 'FLT'
        super().__init__("FLT", value)

class Operation(Token):
    def __init__(self, value):
        # Token pentru operatii matematice sau logice, de exemplu '+', '-', '*', '/'
        super().__init__("OP", value)

class Declaration(Token):
    def __init__(self, value):
        # Token pentru declaratii de variabile, de exemplu 'make'
        super().__init__("DECL", value)

class Variable(Token):
    def __init__(self, value):
        # Token pentru variabile, de exemplu 'x', 'y'
        super().__init__("VAR(?)", value)  # 'VAR(?)' va deveni tipul de variabila dorit, ex: 'VAR(INT)'

class Boolean(Token):
    def __init__(self, value):
        # Token pentru cuvinte cheie boolean, de exemplu 'and', 'or', 'not'
        super().__init__("BOOL", value)

class Comparison(Token):
    def __init__(self, value):
        # Token pentru operatori de comparatie, de exemplu '>', '<', '=='
        super().__init__("COMP", value)

class Reserved(Token):
    def __init__(self, value):
        # Token pentru cuvinte rezervate (ex: 'if', 'while', 'else')
        super().__init__("RSV", value)
