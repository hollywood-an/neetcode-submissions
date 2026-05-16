# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = start = l2
        add = 0
        prev = None
        while head1 and head2:
            val = head1.val + head2.val + add
            if val > 9:
                add = val//10
                val = val%10
            else: 
                add = 0
            head2.val =  val
            head1 = head1.next
            prev = head2
            head2 = head2.next
        print(head1)
        print(head2)
        print(add)
        if head1:
            while head1:
                val = head1.val + add
                if val > 9:
                    add = val//10
                    val = val%10
                else:
                    add = 0
                prev.next = ListNode()
                prev.next.val = val
                prev = prev.next
                head1 = head1.next
        elif head2:
            while head2:
                val = head2.val + add
                if val > 9:
                    add = val//10
                    val = val%10
                else:
                    add = 0
                head2.val = val
                prev = head2
                head2 = head2.next
        print(add)
        if add > 0:
            prev.next = ListNode()
            prev.next.val = add
        return start
        