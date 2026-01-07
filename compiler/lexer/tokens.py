# =========================
# KEYWORDS (DATATYPES)
# =========================

INT     = "INT"
FLOAT   = "FLOAT"
BOOL    = "BOOL"
CHAR    = "CHAR"
STRING  = "STRING"
VOID    = "VOID"

# Other keywords
PRINT   = "PRINT"
TRUE    = "TRUE"
FALSE   = "FALSE"

KEYWORDS = {
    "int": INT,
    "float": FLOAT,
    "bool": BOOL,
    "char": CHAR,
    "string": STRING,
    "void": VOID,
    "print": PRINT,
    "true": TRUE,
    "false": FALSE
}

# =========================
# IDENTIFIERS & LITERALS
# =========================

IDENTIFIER = "IDENTIFIER"

INT_LIT    = "INT_LIT"
FLOAT_LIT  = "FLOAT_LIT"
CHAR_LIT   = "CHAR_LIT"
STRING_LIT = "STRING_LIT"

# =========================
# ARITHMETIC OPERATORS
# =========================

PLUS  = "PLUS"     # +
MINUS = "MINUS"    # -
MUL   = "MUL"      # *
DIV   = "DIV"      # /
MOD   = "MOD"      # %

# =========================
# ASSIGNMENT & RELATIONAL
# =========================

ASSIGN = "ASSIGN"  # =

EQ  = "EQ"         # ==
NEQ = "NEQ"        # !=
LT  = "LT"         # <
GT  = "GT"         # >
LE  = "LE"         # <=
GE  = "GE"         # >=

# =========================
# LOGICAL OPERATORS
# =========================

AND = "AND"        # &&
OR  = "OR"         # ||
NOT = "NOT"        # !

# =========================
# DELIMITERS / SYMBOLS
# =========================

SEMICOLON = "SEMICOLON"   # ;
COMMA     = "COMMA"       # ,

LPAREN = "LPAREN"         # (
RPAREN = "RPAREN"         # )
LBRACE = "LBRACE"         # {
RBRACE = "RBRACE"         # }

# =========================
# SPECIAL
# =========================

EOF = "EOF"
