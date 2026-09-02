class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)    
        longest_consecutive_sequence = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                length = 0 
                while num + length in nums_set:
                    length += 1
                
                longest_consecutive_sequence = max(longest_consecutive_sequence, length)
                
        return longest_consecutive_sequence



        