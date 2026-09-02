class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + '#' + s
        
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            result.append(s[j + 1 : j + 1 + s_len])
            i = j + 1 + s_len
        
        return result



