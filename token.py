from enum import Enum, auto


#Definir los tipos de Token que pueden existir
class TokenType(Enum):
    ID = auto()
    INT_LIT = auto()
    REAL_LIT = auto()
    STRING_LIT = auto()

    # Palabras reservadas
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    RETURN = auto()
    CLASS = auto()
    PUBLIC = auto()
    PRIVATE = auto()
    STATIC = auto()
    INT = auto()
    DOUBLE = auto()
    THIS = auto()
    VOID = auto()
    NEW = auto()

    # Operadores
    ASSIGN = auto()
    EQ = auto()
    NEQ = auto()
    LT = auto()
    GT = auto()
    LE = auto()
    GE = auto()
    PLUS = auto()
    MINUS = auto()
    MULT = auto()
    DIV = auto()

    # Delimitadores
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    SEMICOLON = auto()
    COMMA = auto()  

    # Fin de archivo
    EOF = auto()

class Token:
    def __init__(self, type_: TokenType, value):
        self.type = type_ 
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
    
TokenSpec = [
    (TokenType.IF,       r'\bif\b'),
    (TokenType.ELSE,     r'\belse\b'),
    (TokenType.FOR,      r'\bfor\b'),
    (TokenType.WHILE,    r'\bwhile\b'),
    (TokenType.RETURN,   r'\breturn\b'),
    (TokenType.CLASS,    r'\bclass\b'),
    (TokenType.PUBLIC,   r'\bpublic\b'),
    (TokenType.PRIVATE,  r'\bprivate\b'),
    (TokenType.STATIC,   r'\bstatic\b'),
    (TokenType.INT,      r'\bint\b'),
    (TokenType.DOUBLE,   r'\bdouble\b'),
    (TokenType.VOID,     r'\bvoid\b'),
    (TokenType.THIS,     r'\bthis\b'),
    (TokenType.NEW,      r'\bnew\b'),
    (TokenType.REAL_LIT, r'\d+\.\d+'),
    (TokenType.INT_LIT,  r'\d+'),
    (TokenType.STRING_LIT, r'"([^"\\]|\\.)*"'),
    (TokenType.ID, r'[A-Za-z_][A-Za-z0-9_]*'),
    (TokenType.EQ,     r'=='),
    (TokenType.NEQ,    r'!='),
    (TokenType.LE,     r'<='),
    (TokenType.GE,     r'>='),
    (TokenType.ASSIGN, r'='),
    (TokenType.LT,     r'<'),
    (TokenType.GT,     r'>'),
    (TokenType.PLUS,   r'\+'),
    (TokenType.MINUS,  r'-'),
    (TokenType.MULT,   r'\*'),
    (TokenType.DIV,    r'/'),
    (TokenType.LPAREN,    r'\('),
    (TokenType.RPAREN,    r'\)'),
    (TokenType.LBRACE,    r'\{'),
    (TokenType.RBRACE,    r'\}'),
    (TokenType.SEMICOLON, r';'),
    (TokenType.COMMA,     r','),
]

    
