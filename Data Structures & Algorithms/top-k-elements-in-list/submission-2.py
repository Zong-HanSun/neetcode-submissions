class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        bucket_list = [[] for element in range(len(nums) + 1)]

        for num in hashmap:
            bucket_list[hashmap[num]].append(num)
        
        top_k_frequent = []
        for bucket in reversed(bucket_list):
            if len(top_k_frequent) < k:
                for num in bucket:
                    if len(top_k_frequent) < k:
                        top_k_frequent.append(num)
        
        return top_k_frequent
            


        