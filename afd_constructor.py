from regex_tree import RegexNode, NodeType, RegexTree

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

#Debug para el arbol con la regex seleccionada
my_tree = RegexTree()
my_tree.root = build_tree(to_postfix(insert_concat('(0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*')), my_tree)
my_tree.print_tree(my_tree.root)

