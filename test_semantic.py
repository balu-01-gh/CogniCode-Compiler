from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.semantic.analyzer import SemanticAnalyzer

code = """
int a = 10;
int b = a + 5;
print(b);
"""

lexer = Lexer(code)
parser = Parser(lexer)
ast = parser.parse()

semantic = SemanticAnalyzer()
semantic.analyze(ast)

print("Semantic analysis passed!")
