# compiler/parser/ast_nodes.py

class AST: pass

class Program(AST):
    def __init__(self, statements):
        self.statements = statements

class VarDecl(AST):
    def __init__(self, var_type, name, expr):
        self.var_type = var_type
        self.name = name
        self.expr = expr

class Assign(AST):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class Print(AST):
    def __init__(self, expr):
        self.expr = expr

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Literal(AST):
    def __init__(self, value):
        self.value = value

class Var(AST):
    def __init__(self, name):
        self.name = name
