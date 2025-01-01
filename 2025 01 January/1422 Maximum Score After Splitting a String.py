class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeroCount = 0
        oneCount = 0
        for char in s:
            if char=='1':
                oneCount+=1

        output = 0
        for i in range(0, n-1):
            if s[i]=='0':
                zeroCount+=1
            else:
                oneCount-=1
            output = max(output, zeroCount+oneCount)
        return output