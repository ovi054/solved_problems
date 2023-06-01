class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def getAdj(node):
            p = node[0]
            q = node[1]
            d= node[2]
            adjList =[]
            for i in range(p-1,p+2):
                for j in range(q-1,q+2):
                    if(not isValid(i,j)):
                        continue
                    if(i==p and j==q):
                        continue
                    adjList.append([i,j,d+1])
            return adjList

        def isValid(i,j):
            if(i<0 or i>=n or j<0 or j>=n or grid[i][j]==1):
                return False
            else:
                return True
        
        visited = set()
        if(grid[0][0]==1):
            return -1
        node = [0,0,1]
        queue = deque([node])
        while(queue):
            top = queue.popleft()
            # print("top",top)
            if(top[0]==n-1 and top[1]==n-1):
                return top[2]
            if (top[0],top[1]) in visited:
                continue
            visited.add((top[0],top[1]))
            adjList = getAdj(top)
            # print(adjList)
            for adj in adjList:
                queue.append(adj)
            # print(queue)
        return -1