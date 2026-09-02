class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            alphabet_array = [0] * 26 # each element represents the frequency of a letter in the alphabet
            for char in string:
                index = ord(char) - ord('a')
                alphabet_array[index] += 1
            if tuple(alphabet_array) in hashmap:
                hashmap[tuple(alphabet_array)].append(string)
            else:
                hashmap[tuple(alphabet_array)] = [string]

        return list(hashmap.values())
                
