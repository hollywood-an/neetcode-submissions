# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = None
        counter = 0
        first = None
        start = head 
        while curr is not None:
            if counter == left - 1:
                first = curr
            if counter == right:
                if left == 1:
                    start = prev
                first.next = curr
            if counter >= left and counter < right:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            else:
                prev = curr
                curr = curr.next

            counter += 1


        return start