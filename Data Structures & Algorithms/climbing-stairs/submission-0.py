class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def f(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]

            n_output = f(n - 1) + f(n - 2)
            memo[n] = n_output
            return n_output

        return f(n)