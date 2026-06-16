class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(path, options):
            if not options:
                results.append(path.copy())
                return
            for i in range(len(options)):
                path.append(options[i])
                n = options.copy()
                n.remove(options[i])
                backtrack(path, n)
                path.pop()
        backtrack([], nums)
        return results