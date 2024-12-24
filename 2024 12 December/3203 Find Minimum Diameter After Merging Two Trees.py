class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def createTree(edges):
            hashTable = defaultdict(list)
            for a,b in edges:
                hashTable[a].append(b)
                hashTable[b].append(a)
            return hashTable

        hashTable1 = createTree(edges1)
        hashTable2 = createTree(edges2)


        def findDiameterLength(hashTable):
            queue = deque([0])
            visited = set([0])
            lastNode = 0
            while queue:
                for i in range(len(queue)):
                    top = queue.popleft()
                    for adj in hashTable[top]:
                        if adj not in visited:
                            queue.append(adj)
                            visited.add(adj)
                            lastNode = adj
            # print(0,lastNode)
            queue = deque([lastNode])
            visited = set([lastNode])
            hopp = 0
            while queue:
                for i in range(len(queue)):
                    top = queue.popleft()
                    for adj in hashTable[top]:
                        if adj not in visited:
                            queue.append(adj)
                            visited.add(adj)
                hopp+=1
            return hopp-1

        d1 = findDiameterLength(hashTable1)
        d2 = findDiameterLength(hashTable2)

        # r1 = (d1+1)//2
        # r2 = (d2+1)//2

        # print(d1,d2,r1+r2+1)
        return max(d1,d2, ceil(d1/2)+ceil(d2/2)+1)
    