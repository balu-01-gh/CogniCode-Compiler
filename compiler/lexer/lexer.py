from compiler.lexer.tokens import *

class Token:
    def __init__(self, type_, value=None, line=1):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"{self.type}({self.value})" if self.value is not None else f"{self.type}"


class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1
        self.current_char = source[self.pos] if source else None

    # ------------------
    # Utilities
    # ------------------
    def advance(self):
        self.pos += 1
        self.current_char = self.source[self.pos] if self.pos < len(self.source) else None

    def peek(self):
        nxt = self.pos + 1
        return self.source[nxt] if nxt < len(self.source) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char in " \t":
            self.advance()

    # ------------------
    # Literals
    # ------------------
    def number(self):
        result = ""
        is_float = False

        while self.current_char and (self.current_char.isdigit() or self.current_char == "."):
            if self.current_char == ".":
                if is_float:
                    break
                is_float = True
            result += self.current_char
            self.advance()

        return Token(FLOAT_LIT if is_float else INT_LIT,
                     float(result) if is_float else int(result),
                     self.line)

    def identifier(self):
        result = ""
        while self.current_char and (self.current_char.isalnum() or self.current_char == "_"):
            result += self.current_char
            self.advance()

        return Token(KEYWORDS.get(result, IDENTIFIER), result, self.line)

    def string_literal(self):
        self.advance()  # skip "
        result = ""
        while self.current_char and self.current_char != '"':
            result += self.current_char
            self.advance()

        if self.current_char != '"':
            raise Exception(f"Unterminated string at line {self.line}")

        self.advance()
        return Token(STRING_LIT, result, self.line)

    def char_literal(self):
        self.advance()  # skip '
        value = self.current_char
        self.advance()

        if self.current_char != "'":
            raise Exception(f"Invalid char literal at line {self.line}")

        self.advance()
        return Token(CHAR_LIT, value, self.line)

    # ------------------
    # Main Lexer
    # ------------------
    def get_next_token(self):
        while self.current_char:

            if self.current_char in " \t":
                self.skip_whitespace()
                continue

            if self.current_char == "\n":
                self.line += 1
                self.advance()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char.isalpha() or self.current_char == "_":
                return self.identifier()

            if self.current_char == '"':
                return self.string_literal()

            if self.current_char == "'":
                return self.char_literal()

            # ---- Multi-char operators ----
            if self.current_char == "=" and self.peek() == "=":
                self.advance(); self.advance()
                return Token(EQ, "==", self.line)

            if self.current_char == "!" and self.peek() == "=":
                self.advance(); self.advance()
                return Token(NEQ, "!=", self.line)

            if self.current_char == "<" and self.peek() == "=":
                self.advance(); self.advance()
                return Token(LE, "<=", self.line)

            if self.current_char == ">" and self.peek() == "=":
                self.advance(); self.advance()
                return Token(GE, ">=", self.line)

            if self.current_char == "&" and self.peek() == "&":
                self.advance(); self.advance()
                return Token(AND, "&&", self.line)

            if self.current_char == "|" and self.peek() == "|":
                self.advance(); self.advance()
                return Token(OR, "||", self.line)

            # ---- Single-char operators ----
            char = self.current_char
            self.advance()

            single_char_tokens = {
                "+": PLUS, "-": MINUS, "*": MUL, "/": DIV, "%": MOD,
                "=": ASSIGN, "<": LT, ">": GT, "!": NOT,
                ";": SEMICOLON, ",": COMMA,
                "(": LPAREN, ")": RPAREN,
                "{": LBRACE, "}": RBRACE
            }

            if char in single_char_tokens:
                return Token(single_char_tokens[char], char, self.line)

            raise Exception(f"Illegal character '{char}' at line {self.line}")

        return Token(EOF, None, self.line)
