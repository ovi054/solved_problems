class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = []
        for i in range(m):
            visited.append([])
            for j in range(n):
                visited[i].append(0)

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(i,j):

            if(i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or visited[i][j]==1):
                return 0
            visited[i][j]=1
            val = grid[i][j]
            for a,b in directions:
                i_ = i+a
                j_ = j+b
                val = val + dfs(i_,j_)
            return val

        maxVal = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    maxVal = max(maxVal,dfs(i,j))

        return maxVal
        