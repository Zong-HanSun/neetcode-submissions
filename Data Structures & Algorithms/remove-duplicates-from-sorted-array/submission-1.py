class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                nums.pop(l)
            else:
                r += 1
                l += 1
        return len(nums)
        