class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        n = 0

        def backtrack(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] != "1"
            ):
                return 

            grid[r][c] = "0"

            backtrack(r - 1, c)
            backtrack(r, c + 1)
            backtrack(r + 1, c)
            backtrack(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    backtrack(r, c)
                    n += 1

        return n


        