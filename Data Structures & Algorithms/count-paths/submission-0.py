# dp(r, c) -> from this cell how many different paths can we take to reach bottom right corner?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(r, c):
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            
            # move down
            move_down = dp(r + 1, c)

            # move right
            move_right = dp(r, c + 1)

            ans = move_down + move_right
            memo[(r, c)] = ans
            return ans

        return dp(0, 0)


        