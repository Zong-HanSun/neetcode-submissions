class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        longest_substring = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[r])

            if len(char_set) > longest_substring:
                longest_substring = len(char_set)

        return longest_substring        