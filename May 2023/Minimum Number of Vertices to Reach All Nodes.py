class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*n
        for u,v in edges:
            indegree[v] += 1
        output = []
        for i in range(0,n):
            if(indegree[i]==0):
                output.append(i)
        return output
