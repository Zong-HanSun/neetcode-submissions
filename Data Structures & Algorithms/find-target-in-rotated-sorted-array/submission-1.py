class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # left segment case
            if nums[m] >= nums[r]:
                if target < nums[m]:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    l = m + 1

            # right segment case
            else:
                if target > nums[m]:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    r = m - 1

        return - 1
                    



        