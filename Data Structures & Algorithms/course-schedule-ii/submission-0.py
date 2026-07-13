class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        print(graph)
        visited = set()
        results = []
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            if graph[course] == []:
                results.append(course)
                return True
            for c in graph[course]:
                dfs(c)
            graph[course] = []
        
            results.append(course)
            return True
            
        for i in range(numCourses):
            print(i)
            if not dfs(i):
                print(visited)
                return []
        
        return results