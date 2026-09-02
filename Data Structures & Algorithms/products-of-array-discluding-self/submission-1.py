class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side_total = []
        right_side_total = [1] * len(nums) 
        product_array = []

        for i in range(len(nums)):
            total = 1
            if i == 0:
                left_side_total.append(total)
            else:
                total = nums[i-1] * left_side_total[i-1]
                left_side_total.append(total)

        for i in reversed(range(len(nums))):
            total = 1
            if i == len(nums) - 1:
                right_side_total[i] = total
            else:
                total = nums[i+1] * right_side_total[i+1]
                right_side_total[i] = total
        
        for i in range(len(nums)):
            product_array.append(left_side_total[i] * right_side_total[i])

        return product_array
            

                


        