# dfs(s[i:]) state -> can the substring be segmented into word in dict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if s[i: i + len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i + len(word)] = True
                        return True

            memo[i] = False
            return False
        
        return dfs(0)