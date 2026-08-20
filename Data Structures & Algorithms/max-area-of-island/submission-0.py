class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]==0:
                    q=deque([(i,j)])
                    a=1
                    while q:
                        r,c=q.popleft()
                        visited[r][c]=1
                        for s in range(4):
                            cr=dx[s]+r
                            cc=dy[s]+c
                            if cr>=0 and cr<len(grid) and cc>=0 and cc<len(grid[0]) and grid[cr][cc]==1 and visited[cr][cc]==0:
                                a+=1
                                visited[cr][cc]=1
                                q.append((cr,cc))
                    res=max(res,a)   
        return res                     
