class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        one, two = 0, 1
        for i in range(2, len(nums)):
            nums[i] += max(nums[one:two])
            two += 1


        return max(nums)