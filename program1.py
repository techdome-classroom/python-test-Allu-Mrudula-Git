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
                        q.pop(0)
                        

        return 0
    