from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import io

# Import compiler components
from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.semantic.analyzer import SemanticAnalyzer
from compiler.interpreter.interpreter import Interpreter

app = FastAPI()

# 🔥 THIS IS THE CRITICAL FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow frontend
    allow_credentials=True,
    allow_methods=["*"],        # allows OPTIONS, POST, etc.
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str

@app.post("/run")
def run_code(data: CodeInput):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

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

    except Exception as e:
        return {"error": str(e)}

    finally:
        sys.stdout = old_stdout
