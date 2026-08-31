class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ret = 1000000001
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                s -= nums[left]
                ret = min(ret, r - left + 1)
                left += 1
        if ret > 1000000000:
            return 0
        return ret