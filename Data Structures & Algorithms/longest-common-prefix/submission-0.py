class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for string in strs:
            while not string.startswith(result):
                result = result[:-1]
            
        return result
  

        
        