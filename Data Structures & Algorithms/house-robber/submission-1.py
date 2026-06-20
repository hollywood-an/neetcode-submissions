class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if i%2 == 0:
                one += nums[i]
            else:
                two +=nums[i]

        return max(one, two)  