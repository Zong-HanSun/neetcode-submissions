class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            if i == len(candidates) or total > target:
                return 
            
            # we take
            current.append(candidates[i])
            backtrack(i + 1, current, total + candidates[i])

            # we dont take
            current.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, current, total)
        
        backtrack(0, [], 0)
        return result

