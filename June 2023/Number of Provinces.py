class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        hashTable = defaultdict(set)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if(isConnected[i][j]==1):
                    hashTable[i].add(j)
                    hashTable[j].add(i)
        visited = [False]*n
        def dfs(node):
            if(visited[node]==True):
                return
            visited[node] = True
            for adj in hashTable[node]:
                dfs(adj)
        output = 0
        for i in range(n):
            if(visited[i]==False):
                dfs(i)
                output += 1
        return output