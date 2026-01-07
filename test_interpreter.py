from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.semantic.analyzer import SemanticAnalyzer
from compiler.interpreter.interpreter import Interpreter

code = """
int a = 10;
int b = a + 6 % 4 * 2;
print(b);
"""

# Lexer + Parser
lexer = Lexer(code)
parser = Parser(lexer)
ast = parser.parse()

# Semantic analysis
semantic = SemanticAnalyzer()
semantic.analyze(ast)

# Interpretation
print("Program Output:")
interpreter = Interpreter()
interpreter.interpret(ast)
