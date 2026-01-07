1. What is CogniCode?

CogniCode is NOT based on C, Java, Python, or any existing language.

It is a self-defined language created to demonstrate how programming languages work internally.

Key characteristics:

Custom syntax

Custom grammar

Custom interpreter

No external language dependency

CogniCode exists to teach and demonstrate compiler design concepts, not to replace existing languages.

2. How CogniCode Executes Code

When a program is submitted, it passes through these stages:

Lexer
Converts source code into tokens

Parser
Builds an Abstract Syntax Tree (AST)

Semantic Analyzer
Validates variable usage and rules

Interpreter
Executes the AST directly

There is no bytecode or machine code generation.
Execution happens by walking the AST.

3. Program Structure

A CogniCode program is a sequence of statements.

Rules:

Each statement ends with a semicolon ;

Blocks use { }

Execution is top-to-bottom

Example:
int x = 3;
x = x + 2;
print(x);

Output:
5

4. Supported Data Types

int → integers
float → decimal numbers
bool → true / false
char → single character
string → text

Example:
int a = 10;
float b = 2.5;
bool ok = true;
char c = 'A';
string msg = "Hello";

5. Variables
Declaration

Syntax:
type name = expression;

Example:
int x = 5;

Assignment

Syntax:
name = expression;

Example:
int x = 10;
x = x * 2;
print(x);

Output:
20

6. Print Statement

Used to display output.

Syntax:
print(expression);

Example:
print(100);

Output:
100

7. Arithmetic Operators

Supported operators:

addition

subtraction

multiplication
/ division
% modulo

Example:
int a = 10;
int b = 3;
print(a + b);
print(a % b);

Output:
13
1

8. Comparison Operators

Supported:
== equal
!= not equal
< less than

greater than
<= less or equal
= greater or equal

Example:
int x = 5;
print(x > 3);
print(x == 10);

Output:
true
false

9. Logical Operators

Supported:
&& AND
|| OR
! NOT

Example:
bool result = (true && false);
print(result);

Output:
false

10. If / Else Statements

Syntax:
if (condition) {
statements;
} else {
statements;
}

Example:
int x = 5;

if (x > 3) {
print(1);
} else {
print(0);
}

Output:
1

11. While Loop

Syntax:
while (condition) {
statements;
}

Example:
int i = 0;

while (i < 3) {
print(i);
i = i + 1;
}

Output:
0
1
2

12. break Statement

Immediately exits the loop.

Example:
int i = 0;

while (true) {
print(i);
break;
}

Output:
0

13. continue Statement

Skips the current loop iteration.

Example:
int i = 0;

while (i < 5) {
i = i + 1;

if (i == 3) {
    continue;
}

print(i);


}

Output:
1
2
4
5

14. Unary Operators

Supported:
! logical NOT

numeric negation

Example:
int x = 5;
print(-x);
print(!false);

Output:
-5
true

15. Block Scope

Variables declared inside { } exist only inside that block.

Example:
if (true) {
int x = 10;
print(x);
}

Output:
10

16. Error Handling

CogniCode reports clear semantic and runtime errors.

Example:
print(x);

Output:
Error:
Undefined variable 'x' at line 1

17. Intentional Limitations

The following features are intentionally NOT supported:

Functions

Return statements

Arrays

Classes / objects

Libraries

This keeps the language minimal and focused on core compiler concepts.

18. Why This Project Exists (Interview Answer)

If asked why you built CogniCode:

“I built CogniCode to deeply understand how programming languages work internally.
Instead of using an existing language, I designed my own syntax and grammar and implemented the full compiler pipeline — lexer, parser, semantic analyzer, and interpreter.
This project demonstrates my understanding of AST execution, scope handling, control flow, and error reporting.”

19. Who This Project Is For

Students learning compiler design

Developers curious about language internals

Interview preparation

Educational demonstrations

20. Final Summary

CogniCode is:

Language-agnostic

Interpreter-based

Built completely from scratch

Designed for clarity and learning

This project prioritizes understanding over complexity.

End of CogniCode Manual.