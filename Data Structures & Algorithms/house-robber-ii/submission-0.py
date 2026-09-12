class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}

        def dfs(i, end):
            if i >= end:
                return 0

            if (i, end) in memo:
                return memo[(i, end)]
        
            ans = max(nums[i] + dfs(i + 2, end), dfs(i + 1, end))
            memo[(i, end)] = ans
            return ans
        
        exclude_last = dfs(0, len(nums) - 1)
        exclude_first = dfs(1, len(nums))

        return max(exclude_last, exclude_first)