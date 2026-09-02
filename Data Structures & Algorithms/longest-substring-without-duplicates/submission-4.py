class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0 
        char_set = set()
        l = 0
        for r in range(len(s)):
            if s[r] in char_set:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1

            char_set.add(s[r])
            result = max(result, len(char_set))
            
        return result



        
        