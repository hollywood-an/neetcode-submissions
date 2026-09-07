class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right] and right - left <= k:
                return True
            if right - left <= k:
                right += 1
            else:
                left += 1


        return False