class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplet_list = []

        for i in range(len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] and i > 0:
                continue
            
            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                
                if current_sum == 0:
                    triplet_list.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left+=1
                    right-=1

                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left+=1

                elif current_sum > 0:
                    right-=1
                
                elif current_sum < 0:
                    left+=1
                    
        return triplet_list


    