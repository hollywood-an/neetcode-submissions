class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges == []: return True
        if len(edges) >= n:
            return False
        graph = {i:[] for i in range(n)}
        for node, edge in edges:
            graph[node].append(edge)
            graph[edge].append(node)
        print(graph)
        visited = set()
        def dfs(node):
            if node in visited:
                return True
            if graph[node] == []:
                return True
            visited.add(node)
            for c in graph[node]:
                dfs(c)
            graph[node] = []
            return True
            
        return dfs(0) and len(visited) == n
        