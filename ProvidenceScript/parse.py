class Parser:
    def __init__(self, tokens):
        # Primesti lista de tokens de la lexer
        self.tokens = tokens
        self.idx = 0  # index-ul curent
        self.token = self.tokens[self.idx]  # token-ul curent

    def factor(self):
        # Cea mai de baza unitate dintr-o expresie
        if self.token.type == "INT" or self.token.type == "FLT":
            return self.token
        
        elif self.token.value == "(":
            # Daca expresia e intre paranteze, procesam interiorul
            self.move()
            expression = self.boolean_expression()
            return expression
        
        elif self.token.value == "not":
            # Negare booleana: not <ceva>
            operator = self.token
            self.move()
            output = [operator, self.boolean_expression()]
            return output

        elif self.token.type.startswith("VAR"):
            # Variabila standalone
            return self.token
        
        elif self.token.value == "+" or self.token.value == "-":
            # Operator unar (ex: -x sau +x)
            operator = self.token
            self.move()
            operand = self.boolean_expression()
            return [operator, operand]

    def term(self):
        # Operatii cu prioritate mare: * si /
        left_node = self.factor()
        self.move()
        
        while self.token.value == "*" or self.token.value == "/":
            operator = self.token
            self.move()
            right_node = self.factor()
            self.move()

            # Construim arbore: [stanga, operator, dreapta]
            left_node = [left_node, operator, right_node]

        return left_node

    # <bool_expr> := <comp_expr> and | or | not <comp_expr>

    def if_statement(self):
        # Procesam un singur "if" sau "elif"
        self.move()
        condition = self.boolean_expression()

        if self.token.value == "do":
            self.move()
            action = self.statement()
            return condition, action
        
        elif self.tokens[self.idx - 1].value == "do":
            # In caz ca deja s-a mutat peste "do"
            action = self.statement()
            return condition, action

    def if_statements(self):
        # Gestionam un if + elif-uri + optional un else
        conditions = []
        actions = []

        if_statement = self.if_statement()
        conditions.append(if_statement[0])
        actions.append(if_statement[1])

        while self.token.value == "elif":
            if_statement = self.if_statement()
            conditions.append(if_statement[0])
            actions.append(if_statement[1])

        if self.token.value == "else":
            self.move()
            self.move()  # sarim peste 'do'
            else_action = self.statement()

            return [conditions, actions, else_action]

        return [conditions, actions]

    def while_statement(self):
        # "while <conditie> do <actiune>"
        self.move()
        condition = self.boolean_expression()
        
        if self.token.value == "do":
            self.move()
            action = self.statement()
            return [condition, action]
        
        elif self.tokens[self.idx - 1].value == "do":
            action = self.statement()
            return [condition, action]

    def comp_expression(self):
        # Comparatii: <, >, ==, etc.
        left_node = self.expression()
        while self.token.type == "COMP":
            operator = self.token
            self.move()
            right_node = self.expression()
            left_node = [left_node, operator, right_node]
        
        return left_node

    def boolean_expression(self):
        # Expresii booleene: and, or
        left_node = self.comp_expression()

        while self.token.value == "and" or self.token.value == "or":
            operator = self.token
            self.move()
            right_node = self.comp_expression()
            left_node = [left_node, operator, right_node]

        return left_node

    def expression(self):
        # Operatii adunare/scadere (prioritate mai mica)
        left_node = self.term()
        while self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            right_node = self.term()
            left_node = [left_node, operator, right_node]

        return left_node

    def variable(self):
        # Extrage o variabila daca e valida
        if self.token.type.startswith("VAR"):
            return self.token

    def statement(self):
        # O instructiune poate fi:
        # - declarare de variabila
        # - expresie aritmetica
        # - if sau while
        if self.token.type == "DECL":
            self.move()
            left_node = self.variable()
            self.move()

            if self.token.value == "=":
                operation = self.token
                self.move()
                right_node = self.boolean_expression()
                return [left_node, operation, right_node]

        elif self.token.type in ["INT", "FLT", "OP"] or self.token.value == "not":
            return self.boolean_expression()
        
        elif self.token.value == "if":
            return [self.token, self.if_statements()]
        
        elif self.token.value == "while":
            return [self.token, self.while_statement()]

    def parse(self):
        # Punctul de intrare pt parsing
        return self.statement()

    def move(self):
        # Trecem la urmatorul token
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
