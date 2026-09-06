class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[i]
            ):
                return False

            tmp = board[r][c]
            board[r][c] = '#'

            found = (
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r + 1, c, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            board[r][c] = tmp

            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        
        return False