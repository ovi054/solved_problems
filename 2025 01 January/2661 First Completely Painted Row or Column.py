class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n=len(mat[0])

        columnMap = [0]*n
        rowMap = [0]*m

        hashTable = defaultdict(list)

        for i in range(m):
            for j in range(n):
                hashTable[mat[i][j]] = [i,j]


        for index, val in enumerate(arr):
            i, j  = hashTable[val]
            rowMap[i]+=1
            columnMap[j]+=1

            if rowMap[i]==n or columnMap[j]==m:
                return index