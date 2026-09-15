class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, visited):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'X' or (r, c) in visited): return

            visited.add((r, c))

            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r + 1, c, visited)
            dfs(r, c - 1, visited)


        for r in range(rows):
            dfs(r, 0, visited)
            dfs(r, cols - 1, visited)
        
        for c in range(cols):
            dfs(0, c, visited)
            dfs(rows - 1, c, visited)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    if board[r][c] == 'O':
                        board[r][c] = 'X'

        

        
        
        