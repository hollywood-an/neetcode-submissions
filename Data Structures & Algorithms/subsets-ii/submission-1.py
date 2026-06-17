class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        def backtrack(path, nums):
            if path.copy() not in results: 
                results.append(path.copy())
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path, nums[i+1: len(nums)])
                path.pop()
            return

        backtrack([], nums)
        return results