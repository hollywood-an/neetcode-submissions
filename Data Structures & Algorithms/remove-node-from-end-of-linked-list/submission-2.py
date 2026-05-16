# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        if length == 1:
            return None
        if length == n:
            return head.next
        curr = head
        prev = None
        for i in range(length):
            if i == length-n:
                prev.next = curr.next
                curr = prev.next
                break
            else:
                prev = curr
                curr = curr.next

        return head
        
    def getLength(self, head):
        length = 0
        while head:
            length = length + 1
            head = head.next
        return length