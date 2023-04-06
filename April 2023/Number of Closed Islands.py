#tags: DFS
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j,grid):
            if(i<0 or i>=m or j<0 or j>=n or grid[i][j]==1):
                return
            grid[i][j] = 1
            dfs(i,j-1,grid)
            dfs(i,j+1,grid)
            dfs(i-1,j,grid)
            dfs(i+1,j,grid)
        for i in range(0,m):
            dfs(i,0,grid)
            dfs(i,n-1, grid)
        for j in range(0,n):
            dfs(0,j,grid)
            dfs(m-1,j,grid)
        count = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if(grid[i][j]==0):
                    dfs(i, j, grid)
                    count +=1
        return count
