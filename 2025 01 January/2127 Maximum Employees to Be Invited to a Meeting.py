class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n= len(favorite)
        reverseGraph = defaultdict(list)
        for index, value in enumerate(favorite):
            reverseGraph[value].append(index)

        visited = [0]*n
        isRecursion = [0]*n
        countList =[0]*n

        def dfs(node):
            if node not in reverseGraph:
                return 0
            maxV = 0
            for adj in reverseGraph[node]:
                maxV = max(maxV,1 + dfs(adj))
            # r = 1 + dfs(node.right)
            return maxV

        def isCycleDfs(node, count):
            visited[node] = 1


            countList[node]=count
            count += 1

            adj = favorite[node]
            if visited[adj]==0:
                isCycleDfs(adj,count)

            else:
                countList[node]=count - countList[adj]
            # isRecursion[node]=0
            return countList[node]
        def countCycleLength(start):
            node = start
            count = 0

            # Track the path and visited nodes
            path = []
            while visited[node] == 0:
                visited[node] = 1
                path.append(node)
                countList[node] = count
                node = favorite[node]
                count += 1

            # If we detect a cycle
            if node in path:
                cycle_start_index = path.index(node)
                return len(path) - cycle_start_index  # Cycle length
            return 0  # No cycle

        


        maxCycleLength = 0
        pairedLength = 0
        # print(reverseGraph)
        for i in range(n):
            if visited[i]==0:
                maxCycleLength = max(maxCycleLength,countCycleLength(i))
                # node = i
                # count = 0
                # while(visited[node]==0):
                #     visited[node]=1
                #     countList[node] = count
                #     node = favorite[node]
                #     count+=1
                #     if(visited[node]):
                #         maxCycleLength = max(maxCycleLength,count-countList[node])


       
        for i in range(n):
            fav = favorite[i]
            if favorite[fav]==i and i < favorite[i]:
                node1 =i
                node2 = fav
                
                if node2 in reverseGraph[node1]:
                    reverseGraph[node1].remove(node2)
                if node1 in reverseGraph[node2]:
                    reverseGraph[node2].remove(node1)
                maxNode1 = dfs(node1)
                maxNode2 = dfs(node2)
                pairedLength += maxNode1+maxNode2+2
        # cycleLength = max(countList)
        if maxCycleLength<3:
            maxCycleLength = 0
        # print(countList)
        # print(maxCycleLength)
        return max(maxCycleLength, pairedLength)
        # return 0