# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res=None
        def dfs(root):
            if not root:
                return 0
            m=root==p or root==q
            left=dfs(root.left)
            right=dfs(root.right)
            if m+left+right==2:
                self.res=root
            return m or right or left
        dfs(root)
        return self.res        