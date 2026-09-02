class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        new_array = []
        while len(nums) > 0:
            min_val = min(nums)
            new_array.append(min_val)
            nums.remove(min_val)

        return new_array        