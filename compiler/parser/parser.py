# compiler/parser/parser.py

from compiler.lexer.tokens import *
from compiler.parser.ast_nodes import *


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    # --------------------
    # Utilities
    # --------------------
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(
                f"Expected {token_type}, got {self.current_token.type}"
            )

    def peek_token(self):
        # Save state
        pos = self.lexer.pos
        char = self.lexer.current_char
        tok = self.current_token

        next_tok = self.lexer.get_next_token()

        # Restore state
        self.lexer.pos = pos
        self.lexer.current_char = char
        self.current_token = tok

        return next_tok

    # --------------------
    # Program
    # --------------------
    def parse(self):
        statements = []
        while self.current_token.type != EOF:
            statements.append(self.statement())
        return Program(statements)

    # --------------------
    # Statements
    # --------------------
    def statement(self):
        if self.current_token.type in (INT, FLOAT, BOOL, CHAR, STRING):
            return self.declaration()

        if self.current_token.type == IDENTIFIER:
            next_tok = self.peek_token()

            # assignment
            if next_tok.type == ASSIGN:
                return self.assign_stmt()

            # function call as statement
            if next_tok.type == LPAREN:
                expr = self.expression()
                self.eat(SEMICOLON)
                return expr

            raise Exception("Invalid statement")

        if self.current_token.type == PRINT:
            return self.print_stmt()

        if self.current_token.type == RETURN:
            return self.return_stmt()

        if self.current_token.type == IF:
            return self.if_stmt()

        if self.current_token.type == WHILE:
            return self.while_stmt()

        if self.current_token.type == BREAK:
            tok = self.current_token
            self.eat(BREAK)
            self.eat(SEMICOLON)
            return Break(tok.line)

        if self.current_token.type == CONTINUE:
            tok = self.current_token
            self.eat(CONTINUE)
            self.eat(SEMICOLON)
            return Continue(tok.line)

        raise Exception(
            f"Invalid statement starting with {self.current_token.type}"
        )

    # --------------------
    # Declaration (VAR or FUNCTION)
    # --------------------
    def declaration(self):
        tok = self.current_token
        var_type = tok.type
        self.eat(var_type)

        name_tok = self.current_token
        self.eat(IDENTIFIER)

        # Function declaration
        if self.current_token.type == LPAREN:
            return self.function_decl(var_type, name_tok)

        # Variable declaration
        self.eat(ASSIGN)
        expr = self.expression()
        self.eat(SEMICOLON)
        return VarDecl(var_type, name_tok.value, expr, tok.line)

    # --------------------
    # Function Declaration
    # --------------------
    def function_decl(self, return_type, name_tok):
        self.eat(LPAREN)

        params = []
        if self.current_token.type != RPAREN:
            while True:
                ptype = self.current_token.type
                self.eat(ptype)

                pname_tok = self.current_token
                self.eat(IDENTIFIER)

                params.append((ptype, pname_tok.value))

                if self.current_token.type == COMMA:
                    self.eat(COMMA)
                else:
                    break

        self.eat(RPAREN)
        body = self.block()

        return FunctionDecl(
            return_type,
            name_tok.value,
            params,
            body,
            name_tok.line
        )

    # --------------------
    # Return
    # --------------------
    def return_stmt(self):
        tok = self.current_token
        self.eat(RETURN)
        expr = self.expression()
        self.eat(SEMICOLON)
        return Return(expr, tok.line)

    # --------------------
    # Assignment
    # --------------------
    def assign_stmt(self):
        tok = self.current_token
        name = tok.value
        self.eat(IDENTIFIER)

        self.eat(ASSIGN)
        expr = self.expression()
        self.eat(SEMICOLON)

        return Assign(name, expr, tok.line)

    # --------------------
    # Print
    # --------------------
    def print_stmt(self):
        tok = self.current_token
        self.eat(PRINT)
        self.eat(LPAREN)
        expr = self.expression()
        self.eat(RPAREN)
        self.eat(SEMICOLON)
        return Print(expr, tok.line)

    # --------------------
    # If / While / Block
    # --------------------
    def if_stmt(self):
        tok = self.current_token
        self.eat(IF)
        self.eat(LPAREN)
        condition = self.expression()
        self.eat(RPAREN)
        then_block = self.block()

        else_block = None
        if self.current_token.type == ELSE:
            self.eat(ELSE)
            else_block = self.block()

        return If(condition, then_block, else_block, tok.line)

    def while_stmt(self):
        tok = self.current_token
        self.eat(WHILE)
        self.eat(LPAREN)
        condition = self.expression()
        self.eat(RPAREN)
        body = self.block()
        return While(condition, body, tok.line)

    def block(self):
        tok = self.current_token
        self.eat(LBRACE)

        statements = []
        while self.current_token.type != RBRACE:
            statements.append(self.statement())

        self.eat(RBRACE)
        return Block(statements, tok.line)

    # --------------------
    # Expressions
    # --------------------
    def expression(self):
        return self.logical_or()

    def logical_or(self):
        node = self.logical_and()
        while self.current_token.type == OR:
            tok = self.current_token
            self.eat(OR)
            node = BinOp(node, OR, self.logical_and(), tok.line)
        return node

    def logical_and(self):
        node = self.equality()
        while self.current_token.type == AND:
            tok = self.current_token
            self.eat(AND)
            node = BinOp(node, AND, self.equality(), tok.line)
        return node

    def equality(self):
        node = self.comparison()
        while self.current_token.type in (EQ, NEQ):
            tok = self.current_token
            op = tok.type
            self.eat(op)
            node = BinOp(node, op, self.comparison(), tok.line)
        return node

    def comparison(self):
        node = self.additive()
        while self.current_token.type in (LT, GT, LE, GE):
            tok = self.current_token
            op = tok.type
            self.eat(op)
            node = BinOp(node, op, self.additive(), tok.line)
        return node

    def additive(self):
        node = self.multiplicative()
        while self.current_token.type in (PLUS, MINUS):
            tok = self.current_token
            op = tok.type
            self.eat(op)
            node = BinOp(node, op, self.multiplicative(), tok.line)
        return node

    def multiplicative(self):
        node = self.unary()
        while self.current_token.type in (MUL, DIV, MOD):
            tok = self.current_token
            op = tok.type
            self.eat(op)
            node = BinOp(node, op, self.unary(), tok.line)
        return node

    def unary(self):
        if self.current_token.type == NOT:
            tok = self.current_token
            self.eat(NOT)
            return UnaryOp(NOT, self.unary(), tok.line)

        if self.current_token.type == MINUS:
            tok = self.current_token
            self.eat(MINUS)
            return UnaryOp(MINUS, self.unary(), tok.line)

        return self.primary()

    def primary(self):
        tok = self.current_token

        if tok.type in (INT_LIT, FLOAT_LIT, STRING_LIT, CHAR_LIT):
            self.eat(tok.type)
            return Literal(tok.value, tok.line)

        if tok.type in (TRUE, FALSE):
            self.eat(tok.type)
            return Literal(tok.type == TRUE, tok.line)

        if tok.type == IDENTIFIER:
            name = tok.value
            line = tok.line
            self.eat(IDENTIFIER)

            # Function call
            if self.current_token.type == LPAREN:
                self.eat(LPAREN)
                args = []

                if self.current_token.type != RPAREN:
                    while True:
                        args.append(self.expression())
                        if self.current_token.type == COMMA:
                            self.eat(COMMA)
                        else:
                            break

                self.eat(RPAREN)
                return FunctionCall(name, args, line)

            return Var(name, line)

        if tok.type == LPAREN:
            self.eat(LPAREN)
            node = self.expression()
            self.eat(RPAREN)
            return node

        raise Exception(f"Unexpected token {tok.type}")
