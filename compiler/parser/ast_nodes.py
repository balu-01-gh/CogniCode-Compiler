# compiler/parser/ast_nodes.py

# =========================
# Base Node
# =========================

class ASTNode:
    def __init__(self, line):
        self.line = line


# =========================
# Program / Block
# =========================

class Program(ASTNode):
    def __init__(self, statements):
        super().__init__(line=1)
        self.statements = statements


class Block(ASTNode):
    def __init__(self, statements, line):
        super().__init__(line)
        self.statements = statements


# =========================
# Statements
# =========================

class VarDecl(ASTNode):
    def __init__(self, var_type, name, expr, line):
        super().__init__(line)
        self.var_type = var_type
        self.name = name
        self.expr = expr


class Assign(ASTNode):
    def __init__(self, name, expr, line):
        super().__init__(line)
        self.name = name
        self.expr = expr


class Print(ASTNode):
    def __init__(self, expr, line):
        super().__init__(line)
        self.expr = expr


class If(ASTNode):
    def __init__(self, condition, then_block, else_block, line):
        super().__init__(line)
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block


class While(ASTNode):
    def __init__(self, condition, body, line):
        super().__init__(line)
        self.condition = condition
        self.body = body


class Break(ASTNode):
    def __init__(self, line):
        super().__init__(line)


class Continue(ASTNode):
    def __init__(self, line):
        super().__init__(line)


# =========================
# Expressions
# =========================

class BinOp(ASTNode):
    def __init__(self, left, op, right, line):
        super().__init__(line)
        self.left = left
        self.op = op
        self.right = right


class UnaryOp(ASTNode):
    def __init__(self, op, expr, line):
        super().__init__(line)
        self.op = op
        self.expr = expr


class Literal(ASTNode):
    def __init__(self, value, line):
        super().__init__(line)
        self.value = value


class Var(ASTNode):
    def __init__(self, name, line):
        super().__init__(line)
        self.name = name
# =========================
# FUNCTIONS (Stage 13)
# =========================

class FunctionDecl(ASTNode):
    def __init__(self, return_type, name, params, body, line):
        super().__init__(line)
        self.return_type = return_type   # INT / FLOAT / etc.
        self.name = name                 # function name
        self.params = params             # list of (type, name)
        self.body = body                 # Block


class Return(ASTNode):
    def __init__(self, expr, line):
        super().__init__(line)
        self.expr = expr


class FunctionCall(ASTNode):
    def __init__(self, name, args, line):
        super().__init__(line)
        self.name = name                 # function name
        self.args = args                 # list of expressions
