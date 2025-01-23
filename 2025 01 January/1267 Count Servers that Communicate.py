class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowCount = [0]*m
        columnCount = [0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowCount[i]+=1
                    columnCount[j]+=1
        output = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if rowCount[i]-1> 0 or columnCount[j]-1>0:
                        output+=1
        return output
        