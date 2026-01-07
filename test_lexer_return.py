from compiler.lexer.lexer import Lexer

code = "return x + 1;"

lexer = Lexer(code)

while True:
    token = lexer.get_next_token()
    print(token)
    if token.type == "EOF":
        break
