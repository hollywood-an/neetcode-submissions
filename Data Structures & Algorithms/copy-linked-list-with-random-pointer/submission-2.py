"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = []
        start = head
        og = []
        while head:
            og.append(head)
            copy.append(Node(head.val))
            head = head.next
        for i in range(len(copy)):
            if i+1 < len(copy):
                copy[i].next = copy[i+1]
            if og[i].random:
                copy[i].random = copy[og.index(og[i].random)]
            else:
                copy[i].random = None
        return copy[0]