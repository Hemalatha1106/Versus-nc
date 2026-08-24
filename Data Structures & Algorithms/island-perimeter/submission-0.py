class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    s=4
                    for k in range(4):
                        cr=dx[k]+i
                        cc=dy[k]+j
                        if 0<=cr<len(grid) and 0<=cc<len(grid[0]) and grid[cr][cc]==1:
                            s-=1
                    res+=s
        return res                    
                        