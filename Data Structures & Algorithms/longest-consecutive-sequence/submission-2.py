class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        sorted_nums = sorted(nums)
        global_longest_consecutive_sequence = 1
        local_longest_consecutive_sequence = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                local_longest_consecutive_sequence += 1
            elif sorted_nums[i] == sorted_nums[i-1]:
                continue
            else:
                local_longest_consecutive_sequence = 1

            if local_longest_consecutive_sequence > global_longest_consecutive_sequence:
                global_longest_consecutive_sequence = local_longest_consecutive_sequence
                
        return global_longest_consecutive_sequence


        