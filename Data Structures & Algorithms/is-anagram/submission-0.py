class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k1 = ''.join(sorted(s))
        k2 = ''.join(sorted(t))
        return k1 == k2