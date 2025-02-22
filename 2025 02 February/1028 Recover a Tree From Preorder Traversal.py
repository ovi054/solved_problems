# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = TreeNode()
        n = len(traversal)

        hashTable = defaultdict(list)
        stack =[]
        i = 0
        while(i<n):
            start = i
            count = 0
            while(i<n and not traversal[i].isdigit()):
                count+=1
                i+=1
            num = ''
            while(i<n and traversal[i].isdigit()):
                num+=traversal[i]
                i+=1
            # hashTable[count].append([int(num), start,i-1])
            hashTable[count].append([start,i-1])

        # print(hashTable)


        def breakString(i, j):
            if i>j:
                return -1,-1,-1,-1
            count = 0
            while(i<n and not traversal[i].isdigit()):
                count+=1
                i+=1
            # print(count)
            leftI = i
            leftJ= -1
            rightI = -1
            rightJ = j
            maxStart = -1
            occur = 0
            for start,end in hashTable[count]:
                # print(start,end, i, j)
                if end<=j and end>=i:
                    occur+=1
                    if start>maxStart:
                        maxStart = start
            # print(hashTable[count], occur)
            if occur<=1:
                leftJ = j
                rightI = -1
                rightJ = -1
            else:
                leftJ = maxStart-1
                rightI = maxStart
            return leftI, leftJ, rightI, rightJ

        def findRoot(i):
            while(traversal[i]=='-'):
                i+=1
            out = ''
            while(i<n and traversal[i]!='-'):
                out+=traversal[i]
                i+=1

            return int(out), i


        def solve(i, j, node):
            if i==-1 or j==-1:
                return
            val, nextindex = findRoot(i)
            # print(val)
            # print(nextindex,j)
            node.val = val
            leftI, leftJ, rightI, rightJ = breakString(nextindex, j)
            # print(leftI, leftJ, rightI, rightJ)
            if leftI!=-1 and leftJ!=-1:
                left = TreeNode()
                node.left = left
                solve(leftI, leftJ, node.left)
            
            if rightI!=-1 and rightJ!=-1:
                right = TreeNode()
                node.right = right
                solve(rightI, rightJ, node.right)

            

        solve(0, n-1, root)
        # print(findRoot(0))
        # print(breakString(12,18))

        return root


        