class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        run = [nums[0]]
        for n in nums[1:]:
            run.append(max(n, n*run[-1]))

        return max(run)