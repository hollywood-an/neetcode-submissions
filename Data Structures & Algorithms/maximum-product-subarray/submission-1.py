class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        run = []
        for i in range(len(nums)):
            if i == 0:
                run.append(nums[i])
            if i == 1:
                run.append(nums[i]*run[-1])
                run.append(nums[i])
            if i > 1:
                run.append(nums[i]*run[-1])
                run.append(nums[i]*run[-3])

        print(run)
        return max(run)