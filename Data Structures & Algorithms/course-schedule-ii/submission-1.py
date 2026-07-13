class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited, done = set(), set()
        results = []
        def dfs(course):
            if course in done:
                return True
            if course in visited:
                return False
            visited.add(course)
            for c in graph[course]:
                if not dfs(c):
                    return False
            graph[course] = []
            done.add(course)
            results.append(course)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return results