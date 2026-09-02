class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarray_len = len(nums) + 1
        l = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                curr_subarray_len = r - l + 1
                min_subarray_len = min(curr_subarray_len, min_subarray_len)
                total -= nums[l]
                l += 1
        
        if min_subarray_len != len(nums) + 1:
            return min_subarray_len
        else:
            return 0



            
            
            
