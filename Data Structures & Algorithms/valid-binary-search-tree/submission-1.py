# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            l.append(root.val)
            dfs(root.right)
        dfs(root)
        for i in range(len(l)-1):
            if l[i]>=l[i+1]:
                return False
        return True                