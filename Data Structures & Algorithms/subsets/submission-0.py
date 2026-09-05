class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return 
            
            # we decide to append num
            subset.append(nums[i])
            dfs(i + 1)

            # we decide to skip num
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return result



        