class Solution:
    def minOperations(self, s: str) -> int:
        countA = 0
        countB=0
        toggleA = '0'
        toggleB = '1'
        for i in range(len(s)):
            if(s[i]!=toggleA):
                countA+=1
            if(s[i]!=toggleB):
                countB+=1
            toggleA, toggleB = toggleB, toggleA
        return min(countA,countB)
