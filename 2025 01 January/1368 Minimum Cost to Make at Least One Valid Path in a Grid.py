class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        pq = [] #cost, i, j
        m = len(grid)
        n = len(grid[0])
        result = []
        for i in range(m):
            result.append([])
            for j in range(n):
                result[i].append(inf)
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        heappush(pq, [0,0,0])
        result[0][0] = 0
        while(pq):
            top = heappop(pq)
            cost = top[0]
            i = top[1]
            j = top[2]


            for index, (p,q) in enumerate(direction):
                i_ = i+p
                j_ = j+q
                if(i_>=0 and i_<m and j_>=0 and j_<n):
                    # print(i_,j_)
                    newCost = cost if index==(grid[i][j]-1) else cost+1
                    if(newCost<result[i_][j_]):
                        result[i_][j_] = newCost
                        heappush(pq,[newCost, i_, j_])

        return result[m-1][n-1]