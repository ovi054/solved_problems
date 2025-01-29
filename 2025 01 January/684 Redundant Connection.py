class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n =len(edges)

        graph = defaultdict(list)


        def dfs(node, target, visited):

            if(node==target):
                return True

            visited.add(node)

            for adj in graph[node]:
                if adj not in visited:
                    if dfs(adj, target, visited):
                        return True

            return False

        for a, b in edges:
            if a in graph and b in graph and dfs(a, b, set()):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)


#Solution 2 DSU


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n =len(edges)

        parent = []

        for i in range(n):
            parent.append(i)

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX!=rootY:
                parent[rootY] = x
                return True
            
            else:
                return False

        for a, b in edges:
            if not union(a-1,b-1):
                return [a,b]

            