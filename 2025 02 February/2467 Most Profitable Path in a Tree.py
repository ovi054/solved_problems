class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        hashTable = defaultdict(list)

        for a, b in edges:
            hashTable[a].append(b)
            hashTable[b].append(a)

        n = len(amount)

        visitedBob = [False]*n
        time = [-1]*n


        # def dfsBob(node, path):
        #     # time[node] = t
        #     visitedBob[node]=True
        #     path.append(node)
        #     if node==0:
        #         return path
        #     for adj in hashTable[node]:
        #         if not visitedBob[adj]:
        #             result = dfsBob(adj, path.copy())
        #             if result:
        #                 return result

        # bobPath = dfsBob(bob,[])
        # start = 0
        # for each in bobPath:
        #     time[each] = start
        #     start +=1
        # print(time)

        def dfsBob(node, t):
            visitedBob[node] = True
            if node == 0:
                time[node] = t  # Set time at the root
                return True
            for adj in hashTable[node]:
                if not visitedBob[adj]:
                    if dfsBob(adj, t + 1):
                        time[node] = t  # Set time only if this path leads to 0
                        return True
            return False

        dfsBob(bob,0)

        visitedAlice = [False]*n
        def dfsAlice(node, t, point):
            visitedAlice[node]=True
            newPoint = 0
            if time[node] == -1:  # Bob never reaches here
                newPoint = amount[node]
            elif time[node]<t:
                newPoint= 0
            elif time[node]==t:
                newPoint= amount[node]//2
            else:
                newPoint = amount[node]

            point += newPoint
            adjList = []
            for adj in hashTable[node]:
                if not visitedAlice[adj]:
                    adjList.append(adj)

            if not adjList: #reached the Leaf
                return point

            else:
                maxVal = -math.inf
                for adj in adjList:
                    maxVal = max(maxVal, dfsAlice(adj,t+1, point))
                return maxVal


        return dfsAlice(0, 0,0)
            