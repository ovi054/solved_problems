class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        hashTable = defaultdict(list)

        for a,b in edges:
            hashTable[a].append(b)
            hashTable[b].append(a)

        visited = [False]*n

        def dfs(node, out =[]):
            visited[node] = True
            out.append(node)
            for adj in  hashTable[node]:
                if visited[adj]==False:
                    dfs(adj, out)
            return out
        compList = []
        for i in range(n):
            if visited[i] == False:
                compList.append(dfs(i,[]))

        output = 0

        for comp in compList:
            size = len(comp)
            flag = True
            for node in comp:
                if len(hashTable[node])!=size-1:
                    flag = False
                    break
            if flag:
                output+=1
        return output
