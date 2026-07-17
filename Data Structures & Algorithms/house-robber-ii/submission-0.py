class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        one, two = 0, 0
        for n in nums[1:len(nums)]:
            temp = max(n+one, two)
            one = two
            two = temp
            
        return two