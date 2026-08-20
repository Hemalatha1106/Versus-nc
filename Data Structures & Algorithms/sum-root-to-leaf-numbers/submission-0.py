# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(root,s):
            if not root:
                return
            if not root.left and not root.right:
                s+=str(root.val)
                self.res+=int(s)
                return
            s+=str(root.val)
            dfs(root.left,s)
            dfs(root.right,s)
        dfs(root,"")
        return self.res    
