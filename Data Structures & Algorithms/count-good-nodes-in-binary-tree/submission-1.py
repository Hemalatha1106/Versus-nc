# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.c=0
        def dfs(root,mx):
            if not root:
                return 0
            if root.val>=mx:
                self.c+=1
                mx=max(mx,root.val)
            dfs(root.left,mx)
            dfs(root.right,mx)
        dfs(root,float('-inf'))
        return self.c        

