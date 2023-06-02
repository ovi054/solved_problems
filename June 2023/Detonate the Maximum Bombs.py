class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def getNeighbors(i,visited):
            x1,y1,r1 = bombs[i]
            neigborList = []
            for j in range(0,len(bombs)):
                if(i!=j and visited[j]==False):
                    x2,y2,r2 = bombs[j]
                    d_sq = (x1-x2)**2 +(y1-y2)**2
                    if((r1)**2>=d_sq):
                        neigborList.append(j)
            # print(i,neigborList)
            return neigborList
            
        output = 0
        for i in range(0,len(bombs)):
            count = 1
            visited = [False]*len(bombs)
            queue = deque([i])
            visited[i] = True
            while(queue):
                top = queue.popleft()
                neigborList = getNeighbors(top,visited)
                # print(top,neigborList)
                for neigbor in neigborList:
                        queue.append(neigbor)
                        visited[neigbor] = True
                        count += 1
            if(count>output):
                output = count
        return output
