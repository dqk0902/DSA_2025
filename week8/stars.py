def count_patterns(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    patterns = set()

    def dfs(i, j, pattern):
        if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or grid[i][j] == '.':
            return
        visited[i][j] = True
        pattern.append((i, j))
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                dfs(i + di, j + dj, pattern)

    def normalize_pattern(pattern):
        min_i = min(i for i, j in pattern)
        min_j = min(j for i, j in pattern)
        return tuple(sorted((i - min_i, j - min_j) for i, j in pattern))

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '*' and not visited[i][j]:
                pattern = []
                dfs(i, j, pattern)
                patterns.add(normalize_pattern(pattern))

    return len(patterns)


if __name__ == "__main__":
    grid = ["..*..*..",
            "**.....*",
            ".....**.",
            "...*....",
            ".**....*"]
    print(count_patterns(grid)) # 2

    grid = ["....*..*",
            "*.......",
            "......*.",
            "..*.....",
            "......*."]
    print(count_patterns(grid)) # 1

    grid = ["***.*.**",
            ".*..*..*",
            ".*.***..",
            ".......*",
            "......**"]
    print(count_patterns(grid)) # 4

    grid = ["***.***.",
            "..*...*.",
            "**..**..",
            "..*...*.",
            "**..**.."]
    print(count_patterns(grid)) # 1