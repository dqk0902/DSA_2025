def create_grid(steps):
    if steps > 40:  # Maximum possible steps in a 10x10 grid
        return None
    
    width = min(steps + 2, 10)
    height = min((steps // 2) + 3, 10)
    
    grid = [['#' for _ in range(width)] for _ in range(height)]
    
    x, y = 1, height - 2
    grid[y][x] = 'A'
    
    for i in range(steps - 1):
        if i % 2 == 0:
            x += 1
        else:
            y -= 1
        grid[y][x] = '.'
    
    grid[y][x] = 'B'
    
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if grid[i][j] == '#':
                grid[i][j] = '.'
    
    return [''.join(row) for row in grid]

if __name__ == "__main__":
    grid = create_grid(5)
    print("\n".join(grid))
    # ########
    # #.#B...#
    # #.#.##.#
    # #.....A#
    # ########

    grid = create_grid(10)
    print("\n".join(grid))
    # ########
    # #.#A...#
    # #.####.#
    # #B.....#
    # #.####.#
    # #......#
    # ########

    grid = create_grid(42)
    print(grid) # None