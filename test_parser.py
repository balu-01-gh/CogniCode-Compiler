from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser

code = """
int a = 10 + 6 % 4 * 2;
print(a);
"""

parser = Parser(Lexer(code))
ast = parser.parse()
print(ast)
