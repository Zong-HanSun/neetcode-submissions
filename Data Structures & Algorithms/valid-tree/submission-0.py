class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = {i: [] for i in range(n)}

        for node, nei in edges:
            adj_map[node].append(nei)
            adj_map[nei].append(node)
        
        visited = set()

        def dfs(node, prev_node):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj_map[node]:
                if nei == prev_node:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n