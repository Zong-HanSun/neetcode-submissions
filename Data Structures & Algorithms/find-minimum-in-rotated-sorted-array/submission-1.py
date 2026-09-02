class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            
            k = (l + r) // 2
            res = min(res, nums[k])

            if nums[k] >= nums[r]:
                l = k + 1
            else:
                r = k - 1
        return res


    

        
        