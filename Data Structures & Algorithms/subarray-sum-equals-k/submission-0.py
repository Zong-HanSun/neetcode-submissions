class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        sum = 0
        hashmap = {0 : 1}

        for i in range(len(nums)):
            sum += nums[i]
            prefix_needed = sum - k
            if prefix_needed in hashmap:
                result += hashmap[prefix_needed]
            if sum in hashmap:
                hashmap[sum] += 1
            else:
                hashmap[sum] = 1
        
        return result
            






    


