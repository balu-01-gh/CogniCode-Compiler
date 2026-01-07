# CogniCode 🚀  
**A Compiler Built From Scratch**

CogniCode is a **language-agnostic compiler and interpreter** built completely from scratch to understand how programming languages work internally — from source code to execution.

Instead of compiling an existing language (like C or Java), CogniCode introduces a **custom C-inspired language** to clearly demonstrate every phase of a compiler in a clean, educational, and extensible way.

---

## 🧠 Project Idea & Motivation

Modern developers use programming languages daily, but very few understand **how code is actually processed and executed internally**.

The goal of CogniCode is to:
- Demystify compiler internals
- Build every stage manually without using compiler libraries
- Understand how source code becomes executable behavior

This project was built to **learn by implementing**, not by relying on existing compiler frameworks.

---

## 🧩 What Was Built From Scratch

CogniCode implements the **complete front-end of a compiler** and an **interpreter-based backend**.

### Compiler Pipeline

| Stage | Description | Status |
|-----|------------|------|
| Lexer | Converts source code into tokens | ✅ Implemented |
| Grammar | Formal language rules | ✅ Implemented |
| Parser | Recursive-descent parser | ✅ Implemented |
| AST | Abstract Syntax Tree construction | ✅ Implemented |
| Semantic Analysis | Variable checks & validations | ✅ Implemented |
| Error Handling | Line-aware error messages | ✅ Implemented |
| Execution | Interpreter-based runtime | ✅ Implemented |

➡️ This matches the **standard structure of real-world compilers**.

---

## 🔍 Language Design Philosophy

- The language is **custom-designed**
- Syntax is **C-like** for familiarity
- Semantics are **simple and explicit**
- Focus is on clarity, not complexity

This makes CogniCode **language-agnostic in design** — the compiler pipeline can be extended to support other syntaxes in the future.

---

## ✨ Supported Language Features

### Data Types
- `int`
- `float`
- `bool`
- `char`
- `string`

### Statements
- Variable declaration & assignment
- `print()`

### Control Flow
- `if / else`
- `while`
- `break`
- `continue`

### Expressions
- Arithmetic: `+ - * / %`
- Comparison: `< > <= >= == !=`
- Logical: `&& || !`

---

## 🧪 Example Program

```c
int x = 1;

while (x <= 5) {
    if (x == 3) {
        x = x + 1;
        continue;
    }

    print(x);

    if (x == 4) {
        break;
    }

    x = x + 1;
}

Output
1
2
4

## 📸 Screenshots

![CogniCode Interface](screenshots/screenshot1.png)
![CogniCode Execution](screenshots/screenshot2.png)

---

## ✨ Features

- 🧠 Custom-designed programming language (C-like syntax)
- 🔍 Lexer (tokenization)
- 🌳 Parser with full grammar & precedence
- 🧩 Abstract Syntax Tree (AST)
- ✅ Semantic analysis (basic checks)
- ▶ Interpreter-based execution
- 🔁 Control flow support:
  - `if / else`
  - `while`
  - `break`, `continue`
- 🔢 Arithmetic & logical expressions
- 🧪 Boolean logic (`&&`, `||`, `!`)
- 📍 Line-numbered error reporting
- 🌐 Web-based IDE (Frontend + FastAPI backend)

---

## 🛠 Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | Python |
| Compiler | Custom (Lexer, Parser, AST, Interpreter) |
| API | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Runtime | Interpreter (AST traversal) |

---

## ▶ How to Run

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 2️⃣ Activate Virtual Environment
**Windows:**
```powershell
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3️⃣ Start Backend
```bash
uvicorn backend.main:app --reload
```

### 4️⃣ Open Frontend
Open `frontend/index.html` in your browser.
