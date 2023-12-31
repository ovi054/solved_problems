class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashTable = defaultdict(list)
        maxValue = -1
        for i in range(len(s)):
            current = s[i]
            hashTable[current].append(i)
            value = i - hashTable[current][0] - 1
            if(value>maxValue):
                maxValue = value
        return maxValue
        