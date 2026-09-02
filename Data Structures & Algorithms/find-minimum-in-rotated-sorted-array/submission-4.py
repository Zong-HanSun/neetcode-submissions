class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            min_val = min(min_val, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return min_val