# dp (r, c) state represents min path sum from cell (r, c)



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo = {}

        def dp(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols):
                return float('inf')
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
            

            move_down = dp(r + 1, c)
            move_right = dp(r, c + 1)
            min_sum_path = grid[r][c] + min(move_down, move_right)
            memo[(r, c)] = min_sum_path
            return min_sum_path

        return dp(0, 0)

        



        