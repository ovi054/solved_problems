class Solution:
    output = 0
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        adj = defaultdict(list)
        visited =set()
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def dfs(node):
            sumValue = 0
            for each in adj[node]:
                if each not in visited:
                    # count +=1
                    visited.add(each)
                    sumValue+= dfs(each)
            returnValue = values[node] + sumValue
            if(returnValue%k==0):
                self.output+=1
            return returnValue
        visited.add(0)
        dfs(0)
        result = self.output
        self.output = 0
        return result
