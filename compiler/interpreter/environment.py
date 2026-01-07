class Environment:
    def __init__(self, parent=None):
        self.values = {}
        self.functions = {}
        self.parent = parent

    # -------- Variables --------
    def define(self, name, value):
        self.values[name] = value

    def assign(self, name, value):
        if name in self.values:
            self.values[name] = value
        elif self.parent:
            self.parent.assign(name, value)
        else:
            raise Exception(f"Undefined variable '{name}'")

    def get(self, name):
        if name in self.values:
            return self.values[name]
        if self.parent:
            return self.parent.get(name)
        raise Exception(f"Undefined variable '{name}'")

    # -------- Functions --------
    def define_function(self, name, func):
        self.functions[name] = func

    def get_function(self, name):
        if name in self.functions:
            return self.functions[name]
        if self.parent:
            return self.parent.get_function(name)
        raise Exception(f"Undefined function '{name}'")
