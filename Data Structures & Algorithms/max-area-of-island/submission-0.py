class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def backtrack(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] != 1
            ): return 0

            grid[r][c] = 0
            
            area = 1 + backtrack(r - 1, c) + backtrack(r, c + 1) + backtrack(r + 1, c) + backtrack(r, c - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, backtrack(r, c))
        
        return max_area
        