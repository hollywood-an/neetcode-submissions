class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(current):
            if len(current) == len(nums):
                results.append(current.copy())
                return

            for n in nums:
                if n in current:
                    continue
                current.append(n)
                backtrack(current)
                current.pop()
            
        backtrack([])
        return results