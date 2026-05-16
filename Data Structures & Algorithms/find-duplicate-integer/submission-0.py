class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = set()
        for x in nums:
            if x in n:
                return x
            else:
                n.add(x)