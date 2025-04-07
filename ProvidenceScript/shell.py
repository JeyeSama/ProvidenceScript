from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()

# Bucla principala - REPL (Read, Eval, Print, Loop)

while True:
    text = input("ProvidenceScript: ")

    # 1. Lexing: transformam textul in tokeni

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    # 2. Parsing: transformam tokenii intr-un arbore de sintaxa (tree)

    parser = Parser(tokens)
    tree = parser.parse()

    # 3. Interpretarea (evaluarea) arborelui

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()

    # 4. Afisam rezultatul, daca e ceva de afisat

    if result is not None:
        print(result)
