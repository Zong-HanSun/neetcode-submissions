class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            
            ans = dp(n - 1) + dp(n - 2) + dp(n - 3)
            memo[n] = ans
            return ans
        
        return dp(n)
        