# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = head = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                merged.next = list2
                list2 = list2.next
            else:
                merged.next = list1
                list1 = list1.next
            merged = merged.next
        
        merged.next = list1 if list2 is None else list2
        return head.next
        