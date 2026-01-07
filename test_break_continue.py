from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.interpreter.interpreter import Interpreter

code = """
int i = 0;

while (i < 5) {
    i = i + 1;

    if (i == 2) {
        continue;
    }

    if (i == 4) {
        break;
    }

    print(i);
}
"""

ast = Parser(Lexer(code)).parse()
Interpreter().interpret(ast)
