# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        count = 1
        tempCount = 0
        visited = set()
        output = 0
        while(queue):
            tempCount = 0
            valList = []
            for i in range(count):
                top = queue.popleft()
                if top.left:
                    queue.append(top.left)
                    valList.append(top.left.val)
                    tempCount+=1
                if top.right:
                    queue.append(top.right)
                    valList.append(top.right.val)
                    tempCount+=1

            
            hashTable1 = defaultdict(int)
            # hashTable2 = defaultdict(int)
            for index, val in enumerate(valList):
                hashTable1[val] = index

            sortedValList  = sorted(valList)

            # for index, val in enumerate(sortedValList):
            #     hashTable2[val] = index

            # print(valList)
            tempOut = 0
            for j in range(tempCount):
                if valList[j]!=sortedValList[j]:
                    k = hashTable1[sortedValList[j]]
                    # hashTable2[valList[j]]
                    # k = hashTable2[valList[j]]
                    valList[j],valList[k] = valList[k], valList[j]
                    hashTable1[valList[k]] = k
                    hashTable1[valList[j]] = j
                    tempOut+=1

            output+=tempOut
            count = tempCount
            # print(valList, tempOut)

        return output
        