class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        dirs= [(0,1),(0,-1),(1,0),(-1,0)]
        n= len(grid)
        m= len(grid[0])
        ans= 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]== 'L':
                    ans+=1
                    q= [(i,j)]
                    while(len(q)!=0):
                        p= q[0]
                        grid[p]= 'W'
                        q.pop(0)
                        if(p[0]>0 and grid[p[0]-1][p[1]]=='L'):
                            q.append((p[0]-1, p[1]))
                        if(p[0]<n and grid[p[0]+1][p[1]]=='L'):
                            q.append((p[0]+1, p[1]))
                        if(p[1]>0 and grid[p[0]][p[1]-1]=='L'):
                            q.append()


        return 0
    