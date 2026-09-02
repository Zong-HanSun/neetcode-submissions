class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        list = []

        for j in range(len(nums)):
            remaining = target - nums[j]
            if remaining in hashmap and hashmap[remaining] != j:
                if hashmap[remaining] >= j:
                    list.append(j)
                    list.append(hashmap[remaining])
                    return list
                else:
                    list.append(hashmap[remaining])
                    list.append(j)
                    return list
                

        