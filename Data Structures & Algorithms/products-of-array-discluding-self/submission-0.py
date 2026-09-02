class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_of_array = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
                    j+=1
                else:
                    j+=1
            product_of_array.append(product)

        return product_of_array
            







        