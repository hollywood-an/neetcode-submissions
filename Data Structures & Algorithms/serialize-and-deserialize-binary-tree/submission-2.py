# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        r = []
        def dfs(root):
            if root is None:
                r.append("null")
                return
            r.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        print(" ".join(r))
        return " ".join(r)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        root = data.split(" ")
        self.count = 0
        def dfs():
            if root[self.count] == "null":
                self.count += 1
                return None
            tree = TreeNode(root[self.count])
            self.count += 1
            tree.left = dfs()
            tree.right = dfs()
            return tree
        return dfs()
