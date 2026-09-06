class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()
        
        backtrack([])
        return result


                
                
