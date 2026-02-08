from regex_tree import RegexNode, NodeType, RegexTree
from afd import AFD

def expand_regex(regex):
    return regex + "#"

def insert_concat(regex):
    result = []

    def is_symbol(x):
        return x not in {"|", "*", "(", ")"}

    for i in range(len(regex)):
        result.append(regex[i])

        if i + 1 < len(regex):
            x = regex[i]
            y = regex[i + 1]

            if (is_symbol(x) or x in {")", "*"}) and (is_symbol(y) or y == "("):
                result.append(".")

    return result

precedence = {
    "|": 1,
    ".": 2,
    "*": 3
}

def to_postfix(regex):
    output = []
    stack = []

    for token in regex:
        if token not in precedence and token not in {"(", ")"}:
            output.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()

        else:
            while stack and stack[-1] != "(" and \
                  precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def build_tree(postfix, tree):
    stack = []

    for token in postfix:
        if token == ".":
            right = stack.pop()
            left = stack.pop()
            node = RegexNode(NodeType.CONCAT)
            node.left = left
            node.right = right
            stack.append(node)

        elif token == "|":
            right = stack.pop()
            left = stack.pop()
            node = RegexNode(NodeType.UNION)
            node.left = left
            node.right = right
            stack.append(node)

        elif token == "*":
            child = stack.pop()
            node = RegexNode(NodeType.STAR)
            node.left = child
            stack.append(node)

        else:
            stack.append(tree.new_symbol(token))

    return stack.pop()

def do_nullable_first_last(node):
    if node is None:
        return

    do_nullable_first_last(node.left)
    do_nullable_first_last(node.right)

    if node.node_type == NodeType.SYMBOL:
        node.nullable = False
        node.firstpos = {node.position}
        node.lastpos = {node.position}

    elif node.node_type == NodeType.UNION:
        node.nullable = node.left.nullable or node.right.nullable
        node.firstpos = node.left.firstpos | node.right.firstpos
        node.lastpos = node.left.lastpos | node.right.lastpos

    elif node.node_type == NodeType.CONCAT:
        node.nullable = node.left.nullable and node.right.nullable

        if node.left.nullable:
            node.firstpos = node.left.firstpos | node.right.firstpos
        else:
            node.firstpos = node.left.firstpos

        if node.right.nullable:
            node.lastpos = node.left.lastpos | node.right.lastpos
        else:
            node.lastpos = node.right.lastpos

    elif node.node_type == NodeType.STAR:
        node.nullable = True
        node.firstpos = node.left.firstpos
        node.lastpos = node.left.lastpos

def do_followpos(node, followpos):
    if node is None:
        return

    do_followpos(node.left, followpos)
    do_followpos(node.right, followpos)

    if node.node_type == NodeType.CONCAT:
        for i in node.left.lastpos:
            followpos[i] |= node.right.firstpos

    elif node.node_type == NodeType.STAR:
        for i in node.left.lastpos:
            followpos[i] |= node.left.firstpos

def map_pos_to_symbol(node, mapping):
    if node is None:
        return
    if node.node_type == NodeType.SYMBOL:
        mapping[node.position] = node.value
    map_pos_to_symbol(node.left, mapping)
    map_pos_to_symbol(node.right, mapping)

def build_afd(regex_tree):
    afd = AFD()

    pos_to_symbol = {}
    map_pos_to_symbol(regex_tree.root, pos_to_symbol)
    start_state = frozenset(regex_tree.root.firstpos)
    afd.start_state = start_state
    afd.states.append(start_state)

    unmarked = [start_state]

    end_pos = None
    for pos, sym in pos_to_symbol.items():
        if sym == "#":
            end_pos = pos
            break

    while unmarked:
        S = unmarked.pop()

        symbol_groups = {}
        for p in S:
            sym = pos_to_symbol[p]
            if sym == "#":
                continue
            symbol_groups.setdefault(sym, set()).update(
                regex_tree.followpos[p]
            )

        for sym, U in symbol_groups.items():
            U = frozenset(U)
            if U not in afd.states:
                afd.states.append(U)
                unmarked.append(U)

            afd.transitions[(S, sym)] = U
            
    for state in afd.states:
        if end_pos in state:
            afd.accept_states.add(state)

    return afd

#Debug para el arbol con la regex seleccionada
my_regex = '(0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*'
my_tree = RegexTree()
my_tree.root = build_tree(to_postfix(insert_concat(expand_regex(my_regex))), my_tree)
do_nullable_first_last(my_tree.root)
do_followpos(my_tree.root, my_tree.followpos)
my_tree.print_tree(my_tree.root)
my_afd = build_afd(my_tree)

print("Estados:")
for s in my_afd.states:
    print(s)

print("\nTransiciones:")
for (s, a), t in my_afd.transitions.items():
    print(s, "--", a, "-->", t)

print("\nEstados finales:")
print(my_afd.accept_states)