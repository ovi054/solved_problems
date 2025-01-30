class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:


        graph = defaultdict(list)

        for u,v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        colorList = [-1]*n

        def isDfsBipartite(node, color):
            colorList[node] = color

            for adj in graph[node]:
                if colorList[adj]== colorList[node]:
                    return False
                elif colorList[adj]== -1:
                    adjColor = 1 - colorList[node]
                    if(isDfsBipartite(adj, adjColor)==False):
                        return False
            return True

        #Bipartite Graph Check
        for node in range(n):
            if colorList[node]==-1:
                if(isDfsBipartite(node, 0)==False):
                    return -1

        #BFS level wise traversal
        levelList = [0]*n
        
        def bfs(node):
            visited = [0]*n
            queue = deque([node])
            visited[node]=1
            level = 0

            while(queue):
                size = len(queue)

                while(size!=0):
                    top = queue.popleft()

                    for adj in graph[top]:
                        if visited[adj]==0:
                            visited[adj]=1
                            queue.append(adj)
                    size -=1
                level+=1

            return level

        for node in range(n):
            levelList[node] = bfs(node)

        dfsVisited = [0]*n
        def dfs(node):
            maxLevel  = levelList[node]
            dfsVisited[node] = 1

            for adj in graph[node]:
                if dfsVisited[adj]==0:
                    maxLevel = max(maxLevel,dfs(adj))

            return maxLevel
        output = 0
        for node in range(n):
            if dfsVisited[node]==0:
                output += dfs(node)

        return output


        