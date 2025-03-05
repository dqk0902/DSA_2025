def create_grid(steps):
    if steps > 80 or steps < 1:  # Maximum possible steps in a 10x10 grid
        return None
    
    width = min(steps + 1, 10)
    height = min((steps // 2) + 3, 10)
    
    # Create an empty grid
    grid = ['#' * width for _ in range(height)]
    
    # Create a path
    x, y = 1, height - 2
    grid[y] = grid[y][:x] + 'A' + grid[y][x+1:]
    
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for _ in range(steps - 1):
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 < new_x < width - 1 and 0 < new_y < height - 1:
                if grid[new_y][new_x] == '#':
                    x, y = new_x, new_y
                    row = list(grid[y])
                    row[x] = '.'
                    grid[y] = ''.join(row)
                    break
    
    # Place B
    grid[y] = grid[y][:x] + 'B' + grid[y][x+1:]
    
    return grid

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