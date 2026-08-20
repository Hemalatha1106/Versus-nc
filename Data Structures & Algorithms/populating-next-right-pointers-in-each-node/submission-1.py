"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q=deque([root])
        while q:
            s=len(q)
            l=[]
            for i in range(s):
                cur=q.popleft()
                l.append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)    
            temp=l[0]
            for i in l[1:]:
                temp.next=i
                temp=temp.next
        return root   

                