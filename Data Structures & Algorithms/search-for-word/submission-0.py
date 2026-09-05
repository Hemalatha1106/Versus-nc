class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=[[0]*len(board[0]) for _ in range(len(board))]
        def dfs(r,c,ind):
            if ind>=len(word):
                return True
            dx=[-1,0,1,0]
            dy=[0,1,0,-1]
            for i in range(4):
                cr=r+dx[i]
                cc=c+dy[i]
                if 0<=cr<len(board) and 0<=cc<len(board[0]) and visited[cr][cc]==0 and board[cr][cc]==word[ind]:
                    visited[cr][cc]=1
                    if dfs(cr,cc,ind+1)==True:
                        return True
                    visited[cr][cc]=0
            return False
        for a in range(len(board)):
            for b in range(len(board[0])):
                if board[a][b]==word[0]:
                    visited[a][b]=1
                    if dfs(a,b,1):
                        return True
                    visited[a][b]=0    
        return False                                

