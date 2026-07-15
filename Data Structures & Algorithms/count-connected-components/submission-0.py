class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for node, edge in edges:
            graph[node].append(edge)
            graph[edge].append(node)
        
        components = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            if graph[node] == []:
                return
            visited.add(node)
            for n in graph[node]:
                dfs(n)
            graph[node] = []
            return 1

        for i in range(n):
            if i not in visited:
                components += dfs(i)   
        return components