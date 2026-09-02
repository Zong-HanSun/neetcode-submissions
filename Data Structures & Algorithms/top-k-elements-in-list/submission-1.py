class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else: 
                hashmap[num] += 1
        # sort the hashmap based on values
        sorted_hashmap = dict(sorted(hashmap.items(), key = lambda item: item[1], reverse = True))

        count = 0
        returned_list = []
        for num in sorted_hashmap:
            if count < k:
                returned_list.append(num)
                count += 1
        
        return returned_list


        