from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.interpreter.interpreter import Interpreter

code = """
int a = 10;

if (a > 5) {
    print(1);
} else {
    print(0);
}
"""

ast = Parser(Lexer(code)).parse()
Interpreter().interpret(ast)
