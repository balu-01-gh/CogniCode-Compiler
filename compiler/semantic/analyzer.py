# compiler/semantic/analyzer.py

from compiler.parser.ast_nodes import *
from compiler.semantic.symbol_table import SymbolTable

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, node):
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No semantic rule for {type(node).__name__}")

    # ------------------------
    # AST Visitors
    # ------------------------
    def visit_Program(self, node):
        for stmt in node.statements:
            self.analyze(stmt)

    def visit_VarDecl(self, node):
        expr_type = self.analyze(node.expr)
        self.symbol_table.declare(node.name, node.var_type)

        if expr_type != node.var_type:
            raise Exception(
                f"Type Error: Cannot assign {expr_type} to {node.var_type}"
            )

    def visit_Assign(self, node):
        var_type = self.symbol_table.lookup(node.name)
        expr_type = self.analyze(node.expr)

        if var_type != expr_type:
            raise Exception(
                f"Type Error: Cannot assign {expr_type} to {var_type}"
            )

    def visit_Print(self, node):
        self.analyze(node.expr)

    def visit_BinOp(self, node):
        left_type = self.analyze(node.left)
        right_type = self.analyze(node.right)

        if left_type != right_type:
            raise Exception(
                f"Type Error: {left_type} and {right_type} mismatch"
            )

        return left_type

    def visit_Literal(self, node):
        if isinstance(node.value, int):
            return "INT"
        if isinstance(node.value, float):
            return "FLOAT"
        if isinstance(node.value, str):
            return "STRING"
        if isinstance(node.value, bool):
            return "BOOL"

    def visit_Var(self, node):
        return self.symbol_table.lookup(node.name)
