class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        freq_map = {}
        l = 0

        for r in range(len(s)):
            if s[r] in freq_map:
                freq_map[s[r]] += 1
            else:
                freq_map[s[r]] = 1
            
            max_freq = max(freq_map.values())
            substring_length = r - l + 1
            
            if substring_length - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            else:
                result = max(result, substring_length)

        return result
            


        