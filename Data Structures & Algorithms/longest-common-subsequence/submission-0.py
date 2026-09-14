# text1 = "cat"
# text2 = "crabt"
# given i -> text1 and j -> text2:
# if text1[i] == text2[j], LIS += 1, i + 1, j + 1

# if text1[i] != text2[j], LIS = 0, either i + 1 or j + 1

# i = 1, j = 1 -> "a" != "r"
# j + 1 -> "a" now text1[i] == text2[j + 1]


# dp(i, j) state represents lcs between text1 and text2 from index i and j




class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                ans = 1 + dp(i + 1, j + 1)
                memo[(i, j)] = ans
                return ans

            ans = max(dp(i + 1, j), dp(i, j + 1))
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
        