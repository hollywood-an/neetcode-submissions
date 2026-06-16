class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(path, options):
            s = sum(path)
            if s == target:
                result.append(path.copy())
                return 
            prev = -1
            for i in range (len(options)):
                if s + options[i] > target:
                    continue
                if options[i] == prev:
                    continue
                path.append(options[i])
                backtrack(path, options[i+1:len(options)])
                path.pop()
                prev = options[i]

        backtrack([], candidates)
        return result