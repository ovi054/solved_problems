class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashTable = defaultdict(int)

        for i, j in dominoes:
            if (i,j) in hashTable:
                hashTable[(i,j)]+=1
            else:
                hashTable[(j,i)]+=1
        output = 0
        for key in hashTable.keys():
            n = hashTable[key]
            output+= (n*(n-1))//2

        return output