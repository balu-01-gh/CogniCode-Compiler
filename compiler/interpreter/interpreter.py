from compiler.parser.ast_nodes import *
from compiler.interpreter.environment import Environment
from compiler.errors import CompilerError


# =====================
# Control Flow Signals
# =====================

class BreakSignal(Exception):
    pass


class ContinueSignal(Exception):
    pass


class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value


# =====================
# Interpreter
# =====================

class Interpreter:
    def __init__(self):
        self.env = Environment()

    # -------- Dispatcher --------
    def interpret(self, node):
        method = getattr(self, f"visit_{type(node).__name__}", None)
        if not method:
            raise Exception(f"No execute method for {type(node).__name__}")
        return method(node)

    # -------- Program --------
    def visit_Program(self, node):
        for stmt in node.statements:
            self.interpret(stmt)

    def visit_Block(self, node):
        previous_env = self.env
        self.env = Environment(parent=previous_env)

        for stmt in node.statements:
            self.interpret(stmt)

        self.env = previous_env

    # -------- Statements --------
    def visit_VarDecl(self, node):
        value = self.interpret(node.expr)
        self.env.define(node.name, value)

    def visit_Assign(self, node):
        value = self.interpret(node.expr)
        self.env.assign(node.name, value)

    def visit_Print(self, node):
        print(self.interpret(node.expr))

    def visit_If(self, node):
        if self.interpret(node.condition):
            self.interpret(node.then_block)
        elif node.else_block:
            self.interpret(node.else_block)

    def visit_While(self, node):
        while self.interpret(node.condition):
            try:
                self.interpret(node.body)
            except ContinueSignal:
                continue
            except BreakSignal:
                break

    def visit_Break(self, node):
        raise BreakSignal()

    def visit_Continue(self, node):
        raise ContinueSignal()

    # -------- Functions --------
    def visit_FunctionDecl(self, node):
        self.env.define_function(node.name, node)

    def visit_FunctionCall(self, node):
        func = self.env.get_function(node.name)

        if len(node.args) != len(func.params):
            raise CompilerError(
                f"Function '{node.name}' expects {len(func.params)} arguments, "
                f"got {len(node.args)}",
                line=node.line
            )

        previous_env = self.env
        self.env = Environment(parent=previous_env)

        # params = [(type, name), ...]
        for (_, param_name), arg in zip(func.params, node.args):
            self.env.define(param_name, self.interpret(arg))

        try:
            self.interpret(func.body)
        except ReturnSignal as r:
            self.env = previous_env
            return r.value

        self.env = previous_env
        return None

    def visit_Return(self, node):
        value = self.interpret(node.expr) if node.expr else None
        raise ReturnSignal(value)

    # -------- Expressions --------
    def visit_BinOp(self, node):
        left = self.interpret(node.left)
        right = self.interpret(node.right)

        # Arithmetic
        if node.op == "PLUS":
            return left + right
        if node.op == "MINUS":
            return left - right
        if node.op == "MUL":
            return left * right
        if node.op == "DIV":
            return left / right
        if node.op == "MOD":
            return left % right

        # Comparisons
        if node.op == "LT":
            return left < right
        if node.op == "GT":
            return left > right
        if node.op == "LE":
            return left <= right
        if node.op == "GE":
            return left >= right
        if node.op == "EQ":
            return left == right
        if node.op == "NEQ":
            return left != right

        # 🔥 LOGICAL OPERATORS (THIS WAS MISSING)
        if node.op == "AND":
            return bool(left) and bool(right)
        if node.op == "OR":
            return bool(left) or bool(right)

        raise Exception(f"Unknown operator {node.op}")


    def visit_UnaryOp(self, node):
        value = self.interpret(node.expr)
        if node.op == "NOT": return not value
        if node.op == "MINUS": return -value
        raise Exception("Unknown unary operator")

    def visit_Literal(self, node):
        return node.value

    def visit_Var(self, node):
        return self.env.get(node.name)
