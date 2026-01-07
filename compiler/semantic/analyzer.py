# compiler/semantic/analyzer.py

from compiler.parser.ast_nodes import *
from compiler.errors import CompilerError


class SemanticAnalyzer:
    def __init__(self):
        self.variables = [{}]     # stack of scopes
        self.functions = {}       # function table
        self.current_function = None

    # --------------------
    # Dispatcher
    # --------------------
    def analyze(self, node):
        method = f"visit_{type(node).__name__}"
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise CompilerError(
            f"No semantic rule for {type(node).__name__}",
            line=getattr(node, "line", None)
        )

    # --------------------
    # Program / Block
    # --------------------
    def visit_Program(self, node):
        for stmt in node.statements:
            self.analyze(stmt)

    def visit_Block(self, node):
        self.variables.append({})
        for stmt in node.statements:
            self.analyze(stmt)
        self.variables.pop()

    # --------------------
    # Variables
    # --------------------
    def visit_VarDecl(self, node):
        scope = self.variables[-1]

        if node.name in scope:
            raise CompilerError(
                f"Variable '{node.name}' already declared",
                node.line
            )

        self.analyze(node.expr)
        scope[node.name] = node.var_type

    def visit_Assign(self, node):
        for scope in reversed(self.variables):
            if node.name in scope:
                self.analyze(node.expr)
                return

        raise CompilerError(
            f"Variable '{node.name}' not declared",
            node.line
        )

    def visit_Var(self, node):
        for scope in reversed(self.variables):
            if node.name in scope:
                return

        raise CompilerError(
            f"Variable '{node.name}' not declared",
            node.line
        )

    # --------------------
    # Print
    # --------------------
    def visit_Print(self, node):
        self.analyze(node.expr)

    # --------------------
    # If / While
    # --------------------
    def visit_If(self, node):
        self.analyze(node.condition)
        self.analyze(node.then_block)
        if node.else_block:
            self.analyze(node.else_block)

    def visit_While(self, node):
        self.analyze(node.condition)
        self.analyze(node.body)

    # --------------------
    # 🔥 Function Declaration
    # --------------------
    def visit_FunctionDecl(self, node):
        if node.name in self.functions:
            raise CompilerError(
                f"Function '{node.name}' already defined",
                node.line
            )

        # store function signature
        self.functions[node.name] = {
            "return_type": node.return_type,
            "params": node.params
        }

        # enter function scope
        self.variables.append({})
        self.current_function = node

        # register parameters as variables
        for ptype, pname in node.params:
            if pname in self.variables[-1]:
                raise CompilerError(
                    f"Duplicate parameter '{pname}'",
                    node.line
                )
            self.variables[-1][pname] = ptype

        self.analyze(node.body)

        self.variables.pop()
        self.current_function = None

    # --------------------
    # 🔥 Function Call
    # --------------------
    def visit_FunctionCall(self, node):
        if node.name not in self.functions:
            raise CompilerError(
                f"Function '{node.name}' not defined",
                node.line
            )

        expected = self.functions[node.name]["params"]

        if len(node.args) != len(expected):
            raise CompilerError(
                f"Function '{node.name}' expects {len(expected)} arguments",
                node.line
            )

        for arg in node.args:
            self.analyze(arg)

    # --------------------
    # 🔥 Return
    # --------------------
    def visit_Return(self, node):
        if self.current_function is None:
            raise CompilerError(
                "Return outside function",
                node.line
            )
        self.analyze(node.expr)

    # --------------------
    # Expressions
    # --------------------
    def visit_BinOp(self, node):
        self.analyze(node.left)
        self.analyze(node.right)

    def visit_UnaryOp(self, node):
        self.analyze(node.expr)

    def visit_Literal(self, node):
        pass

    def visit_Break(self, node):
        pass

    def visit_Continue(self, node):
        pass
