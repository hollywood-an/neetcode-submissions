# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        s1 = head
        s2 = prev
        counter = 0
        while s1 and s2:
            temp = s1.next
            s1.next = s2
            temp2 = s2.next
            s2.next = temp
            s1 = temp
            s2 = temp2




        
        

        