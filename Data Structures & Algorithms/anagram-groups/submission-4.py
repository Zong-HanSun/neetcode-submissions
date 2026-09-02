class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            frequency_array = [0] * 26
            for c in s:
                frequency_array[ord(c) - ord('a')] += 1

            if tuple(frequency_array) in hashmap:
                hashmap[tuple(frequency_array)].append(s)
            else:
                hashmap[tuple(frequency_array)] = [s]
        
        return list(hashmap.values())