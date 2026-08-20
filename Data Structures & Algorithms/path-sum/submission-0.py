# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res=False
        def dfs(root,s):
            if not root:
                return
            if not root.left and not root.right:
                s+=root.val
                if s==targetSum:
                    self.res=True    
                return
            dfs(root.left,s+root.val)
            dfs(root.right,s+root.val)
        dfs(root,0)
        return self.res    