class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashTable = defaultdict(int)
        n = len(s)
        for i in range(n):
            hashTable[s[i]] += 1
            hashTable[t[i]] -= 1
        count = 0
        for key in hashTable:
            if hashTable[key] != 0:
                count+= abs(hashTable[key])
        return count//2
        