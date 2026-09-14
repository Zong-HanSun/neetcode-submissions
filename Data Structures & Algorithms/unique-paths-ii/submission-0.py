# dp(r, c) = number of unique ways from this cell we can reach the target

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        memo = {}

        def dp(r, c):
            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]

            # move right
            move_right = dp(r,  c + 1)
            # move down
            move_down = dp(r + 1, c)

            ans = move_right + move_down
            memo[(r, c)] = ans
            return ans

        return dp(0, 0)