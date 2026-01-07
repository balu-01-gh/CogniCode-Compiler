from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.interpreter.interpreter import Interpreter

code = """
print(c);
"""

ast = Parser(Lexer(code)).parse()
Interpreter().interpret(ast)
