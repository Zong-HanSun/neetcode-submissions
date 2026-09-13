
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in memo:
                return memo[amount]
            
            minimum = float("inf")
            
            for coin in coins:
                path = 1 + dfs(amount - coin)
                minimum = min(minimum, path)
            
            memo[amount] = minimum
            return minimum
        
        result = dfs(amount)
        if result == float("inf"):
            return -1
        else:
            return result