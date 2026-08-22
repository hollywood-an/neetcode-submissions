# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = [-1001]
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            m[0] = max(m[0], root.val+left+right, root.val)
            return root.val + max(left, right)
        dfs(root)
        return m[0]