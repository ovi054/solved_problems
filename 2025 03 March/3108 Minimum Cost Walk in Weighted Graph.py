class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        parent = []

        rank = [0]*n

        for i in range(n):
            parent.append(i)


        def union(a,b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                if rank[rootA]>rank[rootB]:
                    parent[rootB] = parent[rootA]
                elif(rank[rootB]<rank[rootA]):
                    parent[rootA] = parent[rootB]
                else:
                    rank[rootA] += 1
                    parent[rootB] = parent[rootA]

        def find(a):
            if a==parent[a]:
                return a
            parent[a] = find(parent[a])
            return parent[a]

        for a,b,val in edges:
            union(a,b)

        groupVal = [-1]*n

        for a,b,val in edges:
            rootA = find(a)
            rootB = find(b)
            groupVal[rootA] = groupVal[rootA]&val

        output = []
        for a,b in query:
            rootA  = find(a)
            rootB =  find(b)
            if rootA == rootB:
                output.append(groupVal[rootA])
            else:
                output.append(-1)


        return output
        