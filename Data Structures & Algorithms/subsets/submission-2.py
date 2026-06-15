class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def backtrack(path, nums):
            results.append(path.copy())
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path, nums[i+1:len(nums)])
                path.pop()

        backtrack([], nums)
        return results