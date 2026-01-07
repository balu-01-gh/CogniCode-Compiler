from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import sys
import io

from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.semantic.analyzer import SemanticAnalyzer
from compiler.interpreter.interpreter import Interpreter
from compiler.errors import CompilerError

app = FastAPI()
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],   # allow frontend
allow_credentials=True,
allow_methods=["*"],   # allow POST, OPTIONS, etc.
allow_headers=["*"],
)


class CodeInput(BaseModel):
    code: str


@app.post("/run")
def run_code(data: CodeInput):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    source_lines = data.code.splitlines()

    try:
        lexer = Lexer(data.code)
        parser = Parser(lexer)
        ast = parser.parse()

        semantic = SemanticAnalyzer()
        semantic.analyze(ast)

        interpreter = Interpreter()
        interpreter.interpret(ast)

        output = sys.stdout.getvalue()
        return {"output": output}

    except CompilerError as e:
        if e.line and 1 <= e.line <= len(source_lines):
            line_text = source_lines[e.line - 1]

            # Try to point caret at the variable/token
            caret_pos = 0
            if "'" in e.message:
                name = e.message.split("'")[1]
                idx = line_text.find(name)
                if idx != -1:
                    caret_pos = idx

            caret = " " * caret_pos + "^"

            return {
                "error": (
                    f"Error at line {e.line}:\n"
                    f"    {line_text}\n"
                    f"    {caret}\n"
                    f"{e.message}"
                )
            }

        return {"error": e.message}

    except Exception as e:
        return {"error": str(e)}

    finally:
        sys.stdout = old_stdout
