class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True

            # left segment
            if nums[m] > nums[r]:
                if target < nums[m]:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    l = m + 1

            # right segment
            elif nums[m] < nums[r]:
                if target > nums[m]:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    r = m - 1
            
            # nums[m] == nums[r]
            else:
                r -= 1

        return False

