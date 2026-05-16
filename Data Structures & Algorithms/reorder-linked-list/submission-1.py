# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = self.getLength(head)
        list1 = ListNode()
        list1start = list1
        list2 = ListNode()
        list2start = list2
        start = head
        for i in range(length):
            temp = start.next
            if i < length/2:
                list1.next = start
                list1 = list1.next
                list1.next = None
            else:
                list2.next = start
                list2 = list2.next
                list2.next = None
            start = temp
        
        curr = list2start.next
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # prev is start of list2
        list1 = list1start.next
        list2 = prev

        while list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2
        
    
    def getLength(self, head):
        length = 0
        while head:
            length = length + 1
            head = head.next
        return length


        
        

        