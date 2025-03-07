class Solution:

    def seive(self, limit):
        primeList = [True]*(limit+1)
        primeList[1] = False
        for i in range(2, int(limit**0.5)+1):
            if primeList[i]==True:
                for j in range(i*i,limit+1,i):
                    primeList[j] = False
        return primeList

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primeList = self.seive(right)
        rangeNums = []
        for i in range(left, right+1):
            if primeList[i]==True:
                rangeNums.append(i)

        if len(rangeNums)<2:
            return [-1,-1]
        
        output = [-1,-1]
        minDiff = inf
        for i in range(1,len(rangeNums)):
            diff = rangeNums[i]-rangeNums[i-1]
            if diff<minDiff:
                minDiff = diff
                output = [rangeNums[i-1],rangeNums[i]]
        return output


