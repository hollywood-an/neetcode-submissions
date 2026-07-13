class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            visited.add(course)
            for c in graph[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True