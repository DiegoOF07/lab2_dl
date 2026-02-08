from enum import Enum, auto

class NodeType(Enum):
    CONCAT = auto()
    UNION = auto()
    STAR = auto()
    SYMBOL = auto()


class RegexNode:
    def __init__(self,node_type: NodeType, value = None, position = None):
        self.value = value
        self.node_type = node_type
        self.position = position #O identificador según lo visto en clase
        self.left = None
        self.right = None
        self.nullable = False
        self.firstpos = set()
        self.lastpos = set()

    def __repr__(self):
        if self.node_type == NodeType.SYMBOL:
            return f"SYMBOL({self.value}, pos={self.position})"
        return f"{self.node_type.name}"

class RegexTree:
    def __init__(self):
        self.root: RegexNode = None
        self.followpos: dict[int, set[int]] = {}
        self._next_pos = 1 #Para llevar el conteo de los identificadores de cada hoja (simbolo)

    def new_symbol(self, value):

        pos = self._next_pos
        self._next_pos += 1

        node = RegexNode(
            node_type=NodeType.SYMBOL,
            value=value,
            position=pos
        )

        self.followpos[pos] = set()
        return node
