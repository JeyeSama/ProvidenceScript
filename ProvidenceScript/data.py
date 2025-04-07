class Data:
    def __init__(self):
        # Initializeaza un dictionar gol
        self.variables = {}

    def read(self, id):
        # Citeste valoarea unei variabile din dictionarul 'variables' folosind cheia 'id'
        return self.variables[id]

    def read_all(self):
        # Returneaza toate variabilele stocate, basically tot dictionaru
        return self.variables

    def write(self, variable, expression):
        # Scrie in dictionarul de variabile
        variable_name = variable.value
        self.variables[variable_name] = expression  # Stocheaza valoarea lui 'expression' pentru variabila 'variable_name'
