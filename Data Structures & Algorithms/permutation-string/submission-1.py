class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        while (right < len(s2) + 1):
            if (sorted(s1) == sorted(s2[left:right])):
                return True
            left += 1
            right += 1
        return False