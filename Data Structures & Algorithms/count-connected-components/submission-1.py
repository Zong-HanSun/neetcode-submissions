class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj_map[n1].append(n2)
            adj_map[n2].append(n1)

        visited = set()
        res = 0

        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj_map[node]:
                dfs(nei)
            
            return True
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res


