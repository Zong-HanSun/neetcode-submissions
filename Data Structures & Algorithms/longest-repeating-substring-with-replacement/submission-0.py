class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_map = {}
        left = 0
        result = 1

        for right in range(len(s)):
            if s[right] not in frequency_map:
                frequency_map[s[right]] = 1
            else:
                frequency_map[s[right]]+= 1

            window_size = right - left + 1
            max_frequency = max(frequency_map.values())
            
            while window_size - max_frequency > k:
                frequency_map[s[left]]-= 1
                left+= 1
                window_size-= 1

            if window_size > result:
                result = window_size

        return result