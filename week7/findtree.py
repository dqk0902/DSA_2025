class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_tree(grid):
    def find_root(grid):
        # Find the root node in the grid
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c].isdigit():
                    # Check if this node has no parent above it
                    if r == 0 or not any(grid[r-1][c].isdigit()):
                        return (r, c)
        return None

    def find_children(grid, root_r, root_c):
        # Determine the possible child locations
        children = []
        
        # Potential child columns for 1 or 2 or 3 children
        child_cols = []
        
        # Search rows below the root
        r = root_r + 1
        while r < len(grid):
            # Check left, straight, and right columns for potential children
            cols_to_check = [root_c-1, root_c, root_c+1]
            
            for col in cols_to_check:
                if 0 <= col < len(grid[r]) and grid[r][col].isdigit():
                    # Verify connection is valid
                    connection_type = grid[r][col-1] if col > 0 else '.'
                    connection_type_right = grid[r][col+1] if col < len(grid[r])-1 else '.'
                    
                    # Check connection type
                    if (col == root_c-1 and connection_type == '/' and connection_type_right in '.|') or \
                       (col == root_c and connection_type_right in '.|' and connection_type in '.|') or \
                       (col == root_c+1 and connection_type_right == '\\' and connection_type in '.|'):
                        child_cols.append((r, col))
            
            # Stop if we've found all connections down from root
            if len(child_cols) == 3:
                break
            
            r += 1
        
        # Create child nodes recursively
        for child_r, child_c in child_cols:
            children.append(find_tree_recursive(grid, child_r, child_c))
        
        return children

    def find_tree_recursive(grid, r, c):
        # Find the value of the current node
        node_value = int(grid[r][c])
        
        # Find and create children
        children = find_children(grid, r, c)
        
        # Create and return node
        return Node(node_value, children)

    # Find the root of the grid and recursively construct the tree
    root_pos = find_root(grid)
    if root_pos is None:
        return None
    
    return find_tree_recursive(grid, root_pos[0], root_pos[1])


if __name__ == "__main__":
    grid = [r"...........",
            r"...........",
            r"......5....",
            r"...../.\...",
            r"....3...\..",
            r"....|....1.",
            r"....2......"]
    tree = find_tree(grid)
    print(tree)
    # Node(5, [Node(3, [Node(2)]), Node(1)])

    grid = [r"....1.....",
            r".../.\....",
            r"..2...\...",
            r"..|....3..",
            r"..7.../|\.",
            r"./.\.4.5.6",
            r"8...9....."]
    tree = find_tree(grid)
    print(tree)
    # Node(1, [Node(2, [Node(7, [Node(8), Node(9)])]), Node(3, [Node(4), Node(5), Node(6)])])