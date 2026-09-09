class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r, c])
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                for nr, nc in directions:
                    new_row = r + nr
                    new_col = c + nc
                    if (
                        new_row < 0 or new_col < 0 or
                        new_row >= rows or new_col >= cols or
                        grid[new_row][new_col] != 1
                    ): continue

                    grid[new_row][new_col] = 2
                    fresh -= 1
                    queue.append([new_row, new_col])

            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1