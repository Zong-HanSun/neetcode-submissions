class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i, current, total):
            if total == target:
                result.append(current.copy())
                return 
            if i >= len(nums) or total > target:
                return 
            
            current.append(nums[i])
            backtrack(i, current, total + nums[i])

            current.pop()
            backtrack(i + 1, current, total)
        
        backtrack(0, [], 0)
        return result
        