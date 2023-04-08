"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#BFS Solution
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        queue = deque([node])
        hashTable = {}
        hashTable[node.val] = Node(node.val,[])
        while(queue):
            top = queue.popleft()
            clone = hashTable[top.val]
            for neighbor in top.neighbors:
                if neighbor.val not in hashTable:
                     hashTable[neighbor.val] = Node(neighbor.val,[])
                     queue.append(neighbor)
                clone.neighbors.append(hashTable[neighbor.val])
        return hashTable[node.val]


#DFS Solution
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        memo = {}
        def dfs(node):
            if(node in memo):
                return memo[node]
            clone = Node(node.val,[])
            memo[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)