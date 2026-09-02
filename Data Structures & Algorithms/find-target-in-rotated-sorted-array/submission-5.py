class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        [3,4,5,6,1,2]

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # we are in left sorted portion
            if nums[m] > nums[r]:
                # target is within l and m
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # we are in right sorted portion
            else:
                # target is within m and r
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return - 1