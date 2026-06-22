"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        stack = [node]
        visited = {node:Node(node.val)}
        while stack:
            n = stack.pop()
            for nb in n.neighbors:
                if nb not in visited:
                    visited[nb] = Node(nb.val)
                    stack.append(nb)
                visited[n].neighbors.append(visited[nb])


        return visited[node]
