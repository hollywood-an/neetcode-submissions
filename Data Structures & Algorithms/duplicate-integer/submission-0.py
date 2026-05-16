class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                print(n)
                return True
            s.add(n)

        return False