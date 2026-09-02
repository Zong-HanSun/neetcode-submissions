class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            sorted_char = sorted(string) # returns list of characters in alphaebtical order
            sorted_string = "".join(sorted_char) # joins the list of char to a new string
            if sorted_string in hashmap:
                hashmap[sorted_string].append(string)
            else:
                hashmap[sorted_string] = [string]

        return (list(hashmap.values()))


        
