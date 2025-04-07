from tokens import Integer, Float, Reserved

class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree  # AST-ul (Abstract Syntax Tree) generat de parser
        self.data = base  # 'base' e baza de date pt variabile (probabil un scope sau context)

    def read_INT(self, value):
        # Converteste valoarea string la int
        return int(value)
    
    def read_FLT(self, value):
        # Converteste valoarea string la float
        return float(value)
    
    def read_VAR(self, id):
        # Citim o variabila folosind ID-ul sau
        variable = self.data.read(id)
        variable_type = variable.type

        # Folosim dynamic dispatch ca sa apelam functia corecta
        return getattr(self, f"read_{variable_type}")(variable.value)

    def compute_bin(self, left, op, right):
        # Calculeaza o operatie binara intre 2 noduri
        left_type = "VAR" if str(left.type).startswith("VAR") else str(left.type)
        right_type = "VAR" if str(right.type).startswith("VAR") else str(right.type)

        if op.value == "=":
            # Daca e o atribuire, schimbam tipul si scriem in context
            left.type = f"VAR({right_type})"
            self.data.write(left, right)
            return self.data.read_all()

        # Extragem valorile reale pt operatiile numerice/logice
        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)

        # Operatii aritmetice si logice
        if op.value == "+":
            output = left + right
        elif op.value == "-":
            output = left - right
        elif op.value == "*":
            output = left * right
        elif op.value == "/":
            output = left / right
        elif op.value == ">":
            output = 1 if left > right else 0
        elif op.value == ">=":
            output = 1 if left >= right else 0
        elif op.value == "<":
            output = 1 if left < right else 0
        elif op.value == "<=":
            output = 1 if left <= right else 0
        elif op.value == "?=":
            output = 1 if left == right else 0
        elif op.value == "and":
            output = 1 if left and right else 0
        elif op.value == "or":
            output = 1 if left or right else 0

        # Returnam Integer sau Float in functie de tipuri
        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)

    def compute_unary(self, operator, operand):
        # Operatii unare: -x, +x, not x
        operand_type = "VAR" if str(operand.type).startswith("VAR") else str(operand.type)
        operand = getattr(self, f"read_{operand_type}")(operand.value)

        if operator.value == "+":
            output = +operand
        elif operator.value == "-":
            output = -operand
        elif operator.value == "not":
            output = 1 if not operand else 0

        return Integer(output) if operand_type == "INT" else Float(output)

    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        # Daca avem un nod de tip lista
        if isinstance(tree, list):
            if isinstance(tree[0], Reserved):
                # Conditie: "if"
                if tree[0].value == "if":
                    for idx, condition in enumerate(tree[1][0]):
                        evaluation = self.interpret(condition)
                        if evaluation.value == 1:
                            return self.interpret(tree[1][1][idx])
                    
                    # Daca avem si un "else"
                    if len(tree[1]) == 3:
                        return self.interpret(tree[1][2])
                    else:
                        return

                # Conditie: "while"
                elif tree[0].value == "while":
                    condition = self.interpret(tree[1][0])
                    
                    while condition.value == 1:
                        # Executam actiunea
                        print(self.interpret(tree[1][1]))

                        # Verificam din nou conditia
                        condition = self.interpret(tree[1][0])
                    
                    return

        # Operatie unara (ex: -x)
        if isinstance(tree, list) and len(tree) == 2:
            expression = tree[1]
            if isinstance(expression, list):
                expression = self.interpret(expression)
            return self.compute_unary(tree[0], expression)
        
        # Daca e doar o valoare/token simplu (ex: un int)
        elif not isinstance(tree, list):
            return tree
        
        else:
            # Operatie binara: [left, operator, right]
            # Recursiv parsam sub-arborii
            left_node = tree[0]
            if isinstance(left_node, list):
                left_node = self.interpret(left_node)

            right_node = tree[2]
            if isinstance(right_node, list):
                right_node = self.interpret(right_node)

            operator = tree[1]
            return self.compute_bin(left_node, operator, right_node)
