class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashTable = defaultdict(int)

        for i in range(1,n+1):
            digitSum = 0
            strVal  = str(i)
            for j in range(0, len(strVal)):
                digitSum+=  int(strVal[j])
            hashTable[digitSum]+=1

        maxLen = 0
        hashTable2 = defaultdict(int)
        for key in hashTable.keys():
            hashTable2[hashTable[key]] +=1
            maxLen = max(maxLen,hashTable[key])
        

        return hashTable2[maxLen]