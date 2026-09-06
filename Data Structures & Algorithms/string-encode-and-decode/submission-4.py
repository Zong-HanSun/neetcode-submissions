class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1

            word_len = int(s[i:j])
            word = s[j + 1: j + 1 + word_len]
            result.append(word)
            i = j + 1 + word_len
            
        return result

            
    