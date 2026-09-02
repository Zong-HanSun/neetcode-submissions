class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        sorted_nums = sorted(nums)
        current_consecutive_sequence = 1
        longest_consecutive_sequence = 1
        previous_integer = sorted_nums[0]

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - previous_integer == 1:
                current_consecutive_sequence +=1
                previous_integer = sorted_nums[i]
                if current_consecutive_sequence > longest_consecutive_sequence:
                    longest_consecutive_sequence = current_consecutive_sequence
            elif sorted_nums[i] - previous_integer == 0:
                previous_integer = sorted_nums[i]

            else:
                current_consecutive_sequence = 1
                previous_integer = sorted_nums[i]

        return longest_consecutive_sequence


        


        
        
        