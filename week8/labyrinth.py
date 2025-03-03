from collections import deque

def find_route(grid):
    rows, cols = len(grid), len(grid[0])
    
    start, end = None, None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)
    
    if not start or not end:
        return None
    
    queue = deque([(start, 0)])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    
    while queue:
        (x, y), dist = queue.popleft()
        
        if (x, y) == end:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and 
                grid[nx][ny] != '#' and (nx, ny) not in visited):
                queue.append(((nx, ny), dist + 1))
                visited.add((nx, ny))
    
    return None 

if __name__ == "__main__":
    grid = ["########",
            "#.#.B..#",
            "#A#.##.#",
            "#......#",
            "########"]
    print(find_route(grid)) # 6

    grid = ["########",
            "#B#...A#",
            "#.#.##.#",
            "#......#",
            "########"]
    print(find_route(grid)) # 9

    grid = ["########",
            "####..B#",
            "#.A#.#.#",
            "#..#...#",
            "########"]
    print(find_route(grid)) # None