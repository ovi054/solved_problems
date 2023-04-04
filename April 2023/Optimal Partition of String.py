class Solution:
    def partitionString(self, s: str) -> int:
        hashTable = {}
        count = 1
        for i in range(len(s)):
            value = s[i]
            if value in hashTable:
                hashTable.clear()
                count += 1
                hashTable[value] = i
            else:
                hashTable[value] = i
        return count
