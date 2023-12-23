class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hashTable = defaultdict(list)
        hashTable[0] = [0]
        curX, curY = 0,0
        for i in range(len(path)):
            print(i,hashTable)
            if path[i]=='N':
                curX += 1
            elif path[i] == 'S':
                curX -= 1
            elif path[i] == 'E':
                curY += 1
            else:
                curY -= 1
            if curX in hashTable:
                if curY in hashTable[curX]:
                    return True
                else:
                    hashTable[curX].append(curY)
            else:
                # hashTable[curX]=[]
                hashTable[curX].append(curY)
        return False
        