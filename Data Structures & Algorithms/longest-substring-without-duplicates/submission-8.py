class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 1
        m = 0
        dic = {}
        if len(s) < 2:
            return len(s)
        while fast < len(s):
            if s[slow] != s[fast] and s[fast] not in dic:
                dic[s[fast]] = fast
                fast = fast + 1
            elif s[fast] in dic:
                if fast - slow > m:
                    m = fast - slow
                slow = fast 
                fast = fast + 1
                dic = {}
            else:
                if fast - slow > m:
                    m = fast - slow
                slow = slow + 1
                fast = slow + 1
                dic = {}
        if m == 0:
            return len(s)
        if fast - slow > m:
            m = fast - slow
        return m