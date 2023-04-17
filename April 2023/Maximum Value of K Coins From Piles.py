#DP, Memoization, TLE-Solution
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        memo = []
        for i in range(0,k+1):
            memo.append({})
        def f(piles,k):
            if(k==0):
                # print("ok", piles)
                return 0
            # print(curVal)
            elif(tuple(map(tuple, piles)) in memo[k]):
                dictVal = memo[k]
                # print("ok")
                return dictVal[tuple(map(tuple, piles))]
            maxVal = -999999
            for i in range(0,len(piles)):
                tempPiles = piles.copy()
                if(len(tempPiles[i])==0):
                    continue
                pileTop = tempPiles[i][0]
                tempPiles[i] = tempPiles[i][1:]
                # print(tempPiles)
                tempVal = pileTop + f(tempPiles,k-1)
                if(tempVal>maxVal):
                    maxVal = tempVal
            tupleList = tuple(map(tuple, piles))
            dictVal = memo[k]
            dictVal[tupleList] = maxVal 
            # memo[k] = dictVal
            # print(memo)
            return maxVal
        return f(piles,k)
