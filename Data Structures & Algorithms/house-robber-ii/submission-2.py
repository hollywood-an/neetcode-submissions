class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        one, two = 0, 0
        for n in nums[1:len(nums)]:
            temp = max(n+one, two)
            one = two
            two = temp
        three, four = 0,0
        for n in nums[0:len(nums)-1]:
            temp = max(n+three, four)
            three = four
            four = temp

        print(two)
        print(four)

        return max(two, four)