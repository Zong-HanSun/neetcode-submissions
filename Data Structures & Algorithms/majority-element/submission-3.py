class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        highest_count = max(hashmap.values())
        
        for key in hashmap:
            if hashmap[key] == highest_count:
                return key
        