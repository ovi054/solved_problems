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

            