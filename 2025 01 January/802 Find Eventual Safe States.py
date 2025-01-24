class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n= len(graph)
        visited = [0]*n
        isRecursion = [0]*n
        def isCycleDfs(node):
            visited[node] = 1
            isRecursion[node] = 1
            for adj in graph[node]:
                if visited[adj]==0 and isCycleDfs(adj):
                    return True
                elif isRecursion[adj] == 1:
                    return True
            isRecursion[node] = 0
            return False
        for i in range(n):
            if visited[i]==0 and isCycleDfs(i):
                pass
        
        output = []
        for i in range(n):
            if isRecursion[i]==0:
                output.append(i)
        return output


        