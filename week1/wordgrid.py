class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def count(self, word):
        total_count = 0
        if len(word) == 1:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.grid[i][j] == word:
                        total_count += 1
            return total_count
        elif self.isPalindrome(word):
            for i in range(self.rows):
                for j in range(self.cols):
                    total_count += self._count_in_direction(i, j, word)
            return total_count // 2
        for i in range(self.rows):
            for j in range(self.cols):
                total_count += self._count_in_direction(i, j, word)
        return total_count

    def _count_in_direction(self, row, col, word):
        count = 0
        for dr, dc in [
            (-1, 0), (1, 0),  
            (0, -1), (0, 1), 
            (-1, -1), (1, 1), 
            (-1, 1), (1, -1)  
        ]:
            if self._check_word_in_direction(row, col, word, dr, dc):
                count += 1
        return count
    
    def _check_word_in_direction(self, row, col, word, dr, dc):
        word_len = len(word)

        for i in range(word_len):
            new_row = row + dr * i
            new_col = col + dc * i
        
            if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
                return False
            if self.grid[new_row][new_col] != word[i]:
                return False
        
        return True
    
    def isPalindrome(self, word):
        return word == word[::-1]

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0    