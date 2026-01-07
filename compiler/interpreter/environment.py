# compiler/interpreter/environment.py

class Environment:
    def __init__(self):
        self.values = {}

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name not in self.values:
            raise Exception(f"Runtime Error: Variable '{name}' not defined")
        return self.values[name]

    def assign(self, name, value):
        if name not in self.values:
            raise Exception(f"Runtime Error: Variable '{name}' not defined")
        self.values[name] = value
