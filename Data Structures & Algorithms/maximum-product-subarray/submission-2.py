class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        run = []
        for i in range(len(nums)):
            if i == 1:
                run.append(nums[i]*run[-1])
            if i > 1:
                run.append(nums[i]*run[-1])
                run.append(nums[i]*run[-3])
            run.append(nums[i])

        print(run)
        return max(run)