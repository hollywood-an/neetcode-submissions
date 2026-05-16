# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, -1001, root.val) and self.helper(root.right, root.val, 1001)

    def helper (self, node, low, high):
        if node is None: 
            return True
        if node.val >= high:
            return False
        if node.val <= low:
            return False
        return self.helper(node.left, low, node.val) and self.helper(node.right, node.val, high)