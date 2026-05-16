# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head is not None:
            if (head.next is None):
                return False
            if (head.val in s):
                return True
            s.add(head.val)
            head = head.next

        return False
