class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(list(set(sorted(nums))))
        print(s)
        if not s:
            return 0
        l1 = []
        l2 = [s[0]]
        for i in range(1, len(s)):
            if ((s[i] - s[i-1]) == 1):
                l2.append(s[i])
            else:
                l1.append(l2)
                l2 = []
                l2.append(s[i])
        l1.append(l2)
        print(l1)
        max = 0
        for j in range(len(l1)):
            if (len(l1[j]) > max):
                max =  len(l1[j])
        return max
