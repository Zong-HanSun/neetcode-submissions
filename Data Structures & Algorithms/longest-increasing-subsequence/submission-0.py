class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev_num):
            if i == len(nums):
                return 0
            if (i, prev_num) in memo:
                return memo[(i, prev_num)]
            
            lis = 0
            if nums[i] > prev_num:
                lis = 1 + dfs(i + 1, nums[i])

            skip = dfs(i + 1, prev_num)
            
            ans = max (lis, skip)
            memo[(i, prev_num)] = ans
            return ans
        
        return dfs(0, float("-inf"))