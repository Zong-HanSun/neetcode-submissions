class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj_map[n1].append(n2)
            adj_map[n2].append(n1)

        visited = set()

        def dfs(node, prev_node):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj_map[node]:
                if nei == prev_node:
                    continue
                if not (dfs(nei, node)):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n