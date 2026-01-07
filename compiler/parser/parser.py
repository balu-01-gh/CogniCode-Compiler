# compiler/parser/parser.py

from compiler.lexer.tokens import *
from compiler.parser.ast_nodes import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    # -------- Utilities --------
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token.type}")

    # -------- Program --------
    def parse(self):
        statements = []
        while self.current_token.type != EOF:
            statements.append(self.statement())
        return Program(statements)

    # -------- Statements --------
    def statement(self):
        if self.current_token.type in (INT, FLOAT, BOOL, CHAR, STRING):
            return self.var_decl()
        if self.current_token.type == IDENTIFIER:
            return self.assign_stmt()
        if self.current_token.type == PRINT:
            return self.print_stmt()
        raise Exception(f"Invalid statement starting with {self.current_token.type}")

    def var_decl(self):
        var_type = self.current_token.type
        self.eat(var_type)

        name = self.current_token.value
        self.eat(IDENTIFIER)

        self.eat(ASSIGN)
        expr = self.expression()
        self.eat(SEMICOLON)

        return VarDecl(var_type, name, expr)

    def assign_stmt(self):
        name = self.current_token.value
        self.eat(IDENTIFIER)

        self.eat(ASSIGN)
        expr = self.expression()
        self.eat(SEMICOLON)

        return Assign(name, expr)

    def print_stmt(self):
        self.eat(PRINT)
        self.eat(LPAREN)
        expr = self.expression()
        self.eat(RPAREN)
        self.eat(SEMICOLON)
        return Print(expr)

    # -------- Expressions (Precedence) --------
    def expression(self):
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            op = self.current_token.type
            self.eat(op)
            node = BinOp(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in (MUL, DIV, MOD):
            op = self.current_token.type
            self.eat(op)
            node = BinOp(node, op, self.factor())
        return node

    def factor(self):
        tok = self.current_token

        if tok.type in (INT_LIT, FLOAT_LIT, STRING_LIT, CHAR_LIT):
            self.eat(tok.type)
            return Literal(tok.value)

        if tok.type in (TRUE, FALSE):
            self.eat(tok.type)
            return Literal(tok.type == TRUE)

        if tok.type == IDENTIFIER:
            self.eat(IDENTIFIER)
            return Var(tok.value)

        if tok.type == LPAREN:
            self.eat(LPAREN)
            node = self.expression()
            self.eat(RPAREN)
            return node

        raise Exception(f"Unexpected token {tok.type}")

