class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for c in preMap[course]:
                if not dfs(c):
                    return False
                else:
                    preMap[course].remove(c)
            return True
            
        return dfs(0)