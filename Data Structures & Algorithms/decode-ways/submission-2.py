# dfs(i) - state -> represents number of ways to decode the substring starting from i
# at each state you have 2 choice:
#     - either consume 1 letter then make a decision on i + 1
#     - or consume 2 letters then make a decision on i + 2

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]

            # consume 1 num to decode
            if s[i] == "0":
                return 0 

            num_ways = dfs(i + 1)
            # consume 2 nums to decode
            if i + 1 < len(s) and int(s[i: i + 2]) <= 26:
                num_ways += dfs(i + 2)
            
            memo[i] = num_ways
            return num_ways

        return dfs(0)
             