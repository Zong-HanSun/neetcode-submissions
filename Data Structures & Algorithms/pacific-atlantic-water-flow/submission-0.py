class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, prev_height, visited):
            if (
                (r, c) in visited or
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                heights[r][c] < prev_height
            ): return

            visited.add((r, c))

            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)

        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(rows - 1, c, heights[rows - 1][c], atlantic)

        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, cols - 1, heights[r][cols - 1], atlantic)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
        


