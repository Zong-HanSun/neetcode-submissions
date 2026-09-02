class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        i = 0
        while i < len(nums):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                i += 1
            else:
                nums.remove(nums[i])
        return len(nums)


        
