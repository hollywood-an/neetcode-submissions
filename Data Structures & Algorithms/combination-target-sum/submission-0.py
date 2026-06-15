class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(path, choices):
            if sum(path) == target:
                result.append(path.copy())
                return
            for i in range(len(choices)):
                if choices[i]+sum(path) > target:
                    continue
                path.append(choices[i])
                backtrack(path, choices[i:len(choices)])
                path.pop()
        backtrack([], nums)
        return result