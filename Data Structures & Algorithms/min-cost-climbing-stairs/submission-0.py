class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = cost[n - 1]

        for r in range(2, n + 1):
            current_floor = n - r

            dp[r] = cost[current_floor] + min(dp[r - 1], dp[r - 2])\

        return min(dp[n], dp[n - 1])
