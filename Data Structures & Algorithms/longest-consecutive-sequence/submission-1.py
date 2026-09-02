class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1

        hashset = set()
        for num in nums:
            hashset.add(num)

        longest_consecutive_sequence = 1

        for num in hashset:
            current_num = num
            current_consecutive_sequence = 1
            if current_num - 1 not in hashset:
                while current_num + 1 in hashset:
                    current_consecutive_sequence +=1
                    current_num +=1
                if current_consecutive_sequence > longest_consecutive_sequence:
                    longest_consecutive_sequence = current_consecutive_sequence

        return longest_consecutive_sequence



                

        