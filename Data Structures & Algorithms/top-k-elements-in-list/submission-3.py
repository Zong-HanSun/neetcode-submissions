class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        array = []
        for num, frequency in hashmap.items():
            array.append([frequency, num])
        array.sort()
        
        result = []
        while len(result) < k:
            result.append(array.pop()[1])        
        return result



            
        
        