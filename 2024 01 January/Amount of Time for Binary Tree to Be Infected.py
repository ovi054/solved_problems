# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        hashTable = defaultdict(list)
        def dfs(node):
            if node is None:
                return
            if node.left:
                hashTable[node.val].append(node.left.val)
                hashTable[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                hashTable[node.val].append(node.right.val)
                hashTable[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            for i in range(len(queue)):
                current = queue.popleft()
                visited.add(current)
                adjList = hashTable[current]
                for adj in adjList:
                    # if adj not in visited:
                    if adj not in visited:
                        queue.append(adj)
            time+=1

        return time

        