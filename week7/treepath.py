class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_path(node, a, b):
    path_to_a = find_path_to_value(node, a, [])
    if path_to_a is None:
        return None
    
    path_to_b = find_path_to_value(node, b, [])
    if path_to_b is None:
        return None
    
    if a == b:
        return [a]
    
    lca_index = find_lca_index(path_to_a, path_to_b)
    
    path_a_to_lca = path_to_a[::-1]
    path_lca_to_b = path_to_b[lca_index:] 

    full_path = path_a_to_lca[:-1] + path_lca_to_b
    
    return full_path

def find_path_to_value(node, target, current_path):
    if node is None:
        return None
    
    current_path = current_path + [node.value]
    
    if node.value == target:
        return current_path
    
    for child in node.children:
        path = find_path_to_value(child, target, current_path)
        if path is not None:
            return path
    
    return None

def find_lca_index(path1, path2):
    lca_index = 0
    for i in range(min(len(path1), len(path2))):
        if path1[i] != path2[i]:
            break
        lca_index = i
    
    return lca_index

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_path(tree1, 3, 2)) # [3, 4, 1, 2]
    print(find_path(tree1, 1, 7)) # [1, 4, 7]
    print(find_path(tree1, 5, 5)) # [5]
    print(find_path(tree1, 7, 3)) # [7, 4, 3]
    print(find_path(tree1, 4, 8)) # None

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_path(tree2, 1, 4)) # [1, 2, 3, 4]
    print(find_path(tree2, 4, 1)) # [4, 3, 2, 1]
    print(find_path(tree2, 2, 3)) # [2, 3]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_path(tree3, 2, 3)) # [2, 1, 3]
    print(find_path(tree3, 1, 2)) # [1, 2]
    print(find_path(tree3, 5, 5)) # None