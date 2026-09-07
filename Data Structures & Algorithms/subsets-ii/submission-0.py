class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, current):
            if i == len(nums):
                result.append(current.copy())
                return
            
            # we take
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
            # explore other path
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, current)


        backtrack(0, [])
        return result