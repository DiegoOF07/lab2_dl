class Token:
    def __init__(self, type_, value):
        self.type = type_ #Tipo de token (ID, NUM_LIT, TEXT_LIT, RESERVED, OP, DELIM)
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
    
