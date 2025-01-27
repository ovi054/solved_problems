class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        hashTable = defaultdict(list)
        for a, b in prerequisites:
            hashTable[a].append(b)

        reach = []
        for i in range(numCourses):
            reach.append([])
            for j in range(numCourses):
                reach[i].append(False)
        print(reach)

        def dfs(start, node):
            for adj in hashTable[node]:
                if not reach[start][adj]:
                    reach[start][adj] = True
                    dfs(start, adj)

        for node in range(numCourses):
            dfs(node, node)

        output = []
        for a, b in queries:
            output.append(reach[a][b])
        return output
        