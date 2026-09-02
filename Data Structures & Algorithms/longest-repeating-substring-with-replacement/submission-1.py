class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        result = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] in freq_map:
                freq_map[s[r]] += 1
            else:
                freq_map[s[r]] = 1
            
            length_window = r - l + 1
            max_freq = max(freq_map.values())
            if length_window - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            else:
                result = max(result, length_window)
                
        return result
