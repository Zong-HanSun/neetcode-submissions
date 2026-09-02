class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sorted_nums = sorted(nums)
        majority_element = sorted_nums[0]
        global_max_counter = 1
        local_counter = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i+1]:
                local_counter += 1
            else:
                local_counter = 1

            if local_counter > global_max_counter:
                global_max_counter = local_counter
                majority_element = sorted_nums[i]
        
        return majority_element
        [2,2,3,4,4,4,4]


        


