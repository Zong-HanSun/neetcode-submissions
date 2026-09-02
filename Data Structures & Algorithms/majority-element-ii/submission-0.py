class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result_array = []
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        condition = len(nums) // 3
        for key in hashmap:
            if hashmap[key] > condition:
                result_array.append(key)
        
        return result_array
        