class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i            
        
        for i in range(len(nums)):
            num_needed = target - nums[i]
            if num_needed in seen and i != seen[num_needed]:
                if i < seen[num_needed]:
                    return [i, seen[num_needed]]
                else:
                    return [seen[num_needed], i]

        