class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        bucket_list = [[] for i in range(len(nums) + 1)]

        for num, freq in hashmap.items():
            bucket_list[freq].append(num)

        result = []

        for i in range(len(bucket_list) - 1 , -1 , - 1):
            for num in bucket_list[i]:
                result.append(num)
                if len(result) == k:
                    return result       
       

       