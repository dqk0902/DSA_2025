def analyze_route(grid):
    start_row, start_col = None, None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'R':
                start_row, start_col = r, c
                break
        if start_row is not None:
            break
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0 
    
    rows, cols = len(grid), len(grid[0])
    visited = {(start_row, start_col)} 
    
    row, col = start_row, start_col
    
    state_history = {(row, col, current_dir)}
    
    while True:
        dr, dc = directions[current_dir]
        next_row, next_col = row + dr, col + dc
        
        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
            return (len(visited), True)
        
        if grid[next_row][next_col] == '#':
            current_dir = (current_dir + 1) % 4
            state = (row, col, current_dir)
            if state in state_history:
                return (len(visited), False)
            state_history.add(state)
        else:
            row, col = next_row, next_col
            visited.add((row, col))
            
            state = (row, col, current_dir)
            if state in state_history:
                return (len(visited), False)
            state_history.add(state)

if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1))  # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2))  # (12, False)
    
    grid3 = ["##",
             "#R"]
    print(analyze_route(grid3))  # (1, True)