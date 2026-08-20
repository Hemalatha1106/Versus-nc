# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        t=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if root.val!=key:
                t.append(root.val)
            dfs(root.right)
        dfs(root)
        def build(l,r):
            if l>r:
                return
            m=(l+r)//2
            root=TreeNode(t[m])
            root.left=build(l,m-1)
            root.right=build(m+1,r)
            return root
        return build(0,len(t)-1)        
                