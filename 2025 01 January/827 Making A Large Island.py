class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # visitedClone = []

        # for i in range(m):
        #     visitedClone.append([])
        #     for j in range(n):
        #         visitedClone[i].append(0)


        groupLengthList = [[0] * n for _ in range(m)]

        hashTable = defaultdict(int)

        visited = [[0] * n for _ in range(m)]

        def dfs(i,j, uniqueId):

            if(i<0 or i>=m or j<0 or j>=n or visited[i][j]==1 or grid[i][j]==0):
                return 0

            visited[i][j] = 1
            grid[i][j] = uniqueId


            length = 1

            for a,b in directions:
                i_ = i+a
                j_ = j+b
                length  = length + dfs(i_,j_, uniqueId)

            return length

        
        maxVal = 0
        uniqueId = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    length = dfs(i,j, uniqueId)
                    hashTable[uniqueId] = length
                    uniqueId+=1
                    maxVal = max(maxVal, length)
                    


        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    length = 1
                    uniqueSet = set()
                    for a,b in directions:
                        i_ = i +a
                        j_ = j+ b
                        if(i_>=0 and i_<m and j_>=0 and j_<n):
                            uniqueSet.add(grid[i_][j_])
                    for each in uniqueSet:
                        length+= hashTable[each]


                    maxVal = max(maxVal, length)


        return maxVal

