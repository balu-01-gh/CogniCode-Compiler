# compiler/interpreter/interpreter.py

from compiler.parser.ast_nodes import *
from compiler.interpreter.environment import Environment

class Interpreter:
    def __init__(self):
        self.env = Environment()

    def interpret(self, node):
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No execute method for {type(node).__name__}")

    # --------------------
    # AST Visitors
    # --------------------
    def visit_Program(self, node):
        for stmt in node.statements:
            self.interpret(stmt)

    def visit_VarDecl(self, node):
        value = self.interpret(node.expr)
        self.env.define(node.name, value)

    def visit_Assign(self, node):
        value = self.interpret(node.expr)
        self.env.assign(node.name, value)

    def visit_Print(self, node):
        value = self.interpret(node.expr)
        print(value)

    def visit_BinOp(self, node):
        left = self.interpret(node.left)
        right = self.interpret(node.right)

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

        raise Exception(f"Unknown operator {node.op}")

    def visit_Literal(self, node):
        return node.value

    def visit_Var(self, node):
        return self.env.get(node.name)
