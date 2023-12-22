class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        oneCount = 0
        for i in range(n):
            if(s[i]=='1'):
                oneCount += 1
        zeroCount = 0
        maxCount = 0
        for i in range(0,n-1):
            if(s[i]=='0'):
                zeroCount += 1
            else:
                oneCount -= 1
            if zeroCount+oneCount>maxCount:
                 maxCount = zeroCount+oneCount
        return maxCount
        # for i in range(n-1):
        #     if(s[i]=='0'):
        #         zeroCount+=1
        #     oneCount = 0
        #     for j in range(i+1,n):
        #         if(s[j]=='1'):
        #             oneCount+=1
        #     # print(i,zeroCount,oneCount)
        #     if zeroCount+oneCount>maxCount:
        #         maxCount = zeroCount+oneCount
        # return maxCount

        