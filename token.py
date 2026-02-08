from enum import Enum, auto


#Definir los tipos de Token que pueden existir
class TokenType(Enum):
    ID = auto()
    NUM_LIT = auto()
    TEXT_LIT = auto()
    RESERVED = auto()
    OP = auto()
    DELIM = auto()

class Token:
    def __init__(self, type_: TokenType, value):
        self.type = type_ #Tipo de token (ID, NUM_LIT, TEXT_LIT, RESERVED, OP, DELIM)
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
    
TokenSpec = [
    (TokenType.ID, r'[a-zA-Z_][a-zA-Z0-9_]*'), #Empezar con letra o guion y luego pueden tener lo que sea
    (TokenType.NUM_LIT, r'[-+]?\d+(\.\d+)?'), #Numeros enteros o decimales
    (TokenType.TEXT_LIT, r'"([^"\\]|\\.)*"'), #Cadenas de texto entre comillas
    (TokenType.RESERVED, r'\b(if|else|for|return|public|private|class|static|int|double|this)\b'), #Palabras reservadas
    (TokenType.OP, r'[+\-*/=]'), #Operadores aritméticos y de asignación
    (TokenType.DELIM, r'[(){};,]'), #Delimitadores
]

    
