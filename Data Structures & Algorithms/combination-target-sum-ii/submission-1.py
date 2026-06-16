class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(path, options):
            if sum(path) == target and path.copy() not in result:
                result.append(path.copy())
                return 
            
            for i in range (len(options)):
                if sum(path) + options[i] > target:
                    continue
                path.append(options[i])
                backtrack(path, options[i+1:len(options)])
                path.pop()

        backtrack([], candidates)
        return result