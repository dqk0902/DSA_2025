class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def ancestor(node, a, b):
    def find_path(current, target, path):
        if current.value == target:
            return path + [current.value]
        for child in current.children:
            result = find_path(child, target, path + [current.value])
            if result:
                return result
        return None

    path_a = find_path(node, a, [])
    path_b = find_path(node, b, [])

    if not path_a or not path_b:
        return False

    return a in path_b and path_a[-1] == a

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(ancestor(tree1, 1, 3)) # True
    print(ancestor(tree1, 2, 6)) # True
    print(ancestor(tree1, 3, 1)) # False
    print(ancestor(tree1, 5, 6)) # False
    print(ancestor(tree1, 3, 3)) # True

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(ancestor(tree2, 1, 4)) # True
    print(ancestor(tree2, 3, 2)) # False

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(ancestor(tree3, 1, 2)) # True
    print(ancestor(tree3, 1, 1)) # True
    print(ancestor(tree3, 2, 1)) # False
    print(ancestor(tree3, 5, 5)) # False