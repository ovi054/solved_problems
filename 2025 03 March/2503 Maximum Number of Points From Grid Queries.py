class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        directions = [(-1,0), (0,-1),(1,0), (0,1)]
        
        m = len(grid)
        n = len(grid[0])

        def getNeighbors(i,j, target):
            neighbors = []
            for p, q in directions:
                if i+p<m and i+p>=0 and j+q<n and j+q>=0 and visited[i+p][j+q]==0:
                    i_ = i+p
                    j_= j+ q
                    neighbors.append([i_,j_])

            # neighborsPair = sorted(neighborsPair)

            # out = []

            # for val, neighbor in neighborsPair:
            #     out.append(neighbor)

            return neighbors


        hashTable = defaultdict(int)

        for i,query in enumerate(queries):
            hashTable[query] = i

        sortedQueries = sorted(queries)

        visited = []

        for i in range(m):
            visited.append([])
            for j in range(n):
                visited[i].append(0)


        def processQuery(minHeap, target):
            out = 0
            while minHeap and minHeap[0][0]<target:
                out+=1
                val, indexList = heappop(minHeap)
                topI, topJ = indexList


                neighbors = getNeighbors(topI, topJ,target)

                for i_,j_ in neighbors:
                    heappush(minHeap, [grid[i_][j_], [i_,j_]])
                    visited[i_][j_] = 1

            return out

            

        queryOutput = defaultdict(int)

        curOut = 0

        minHeap = []

        heappush(minHeap, [grid[0][0],[0,0]])
        visited[0][0] = 1


        for query in sortedQueries:
            sumValue = processQuery(minHeap, query)
            # print(sumValue)
            curOut+=sumValue
            queryOutput[query] = curOut

        output = []

        for query in queries:
            output.append(queryOutput[query])

        return output
