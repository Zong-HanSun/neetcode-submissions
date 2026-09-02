class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        char_seen = set()
        l = 0
        
        for r in range(len(s)):
            while s[r] in char_seen:
                char_seen.remove(s[l])
                l += 1

            char_seen.add(s[r])
            result = max(result, len(char_seen))
        
        return result




        