# compiler/semantic/symbol_table.py

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, name, var_type):
        if name in self.symbols:
            raise Exception(f"Semantic Error: Variable '{name}' already declared")
        self.symbols[name] = var_type

    def lookup(self, name):
        if name not in self.symbols:
            raise Exception(f"Semantic Error: Variable '{name}' not declared")
        return self.symbols[name]
