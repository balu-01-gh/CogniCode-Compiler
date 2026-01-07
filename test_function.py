from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.semantic.analyzer import SemanticAnalyzer
from compiler.interpreter.interpreter import Interpreter

code = """
int add(int a, int b) {
    return a + b;
}

int x = add(3, 4);
print(x);
"""

lexer = Lexer(code)
parser = Parser(lexer)
ast = parser.parse()

semantic = SemanticAnalyzer()
semantic.analyze(ast)

interpreter = Interpreter()
interpreter.interpret(ast)
