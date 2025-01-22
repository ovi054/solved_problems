class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        output = isWater
        m = len(isWater)
        n = len(isWater[0])
        visited = []
        for i in range(m):
            visited.append([])
            for j in range(n):
                visited[i].append(0)
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    queue.append((i,j,0))
                    visited[i][j] = 1

        def findAdjacent(i, j):
            out = []
            if i-1>=0 and visited[i-1][j]==0:
                out.append([i-1,j])
            if i+1<m and visited[i+1][j]==0:
                out.append([i+1,j])
            if j-1>=0 and visited[i][j-1]==0:
                out.append([i,j-1])
            if j+1<n and visited[i][j+1]==0:
                out.append([i,j+1])
            return out

        while(queue):
            i,j, val = queue.popleft()
            output[i][j] = val
            adjList = findAdjacent(i,j)
            for i_,j_ in adjList:

                queue.append([i_,j_,val+1])
                visited[i_][j_] = 1

        return output



