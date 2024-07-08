class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        valList = []
        for i in range(1,n+1):
            valList.append(i)
        index = 0
        while(len(valList)>1):
            index = (index+k-1)%len(valList)
            valList.pop(index)
        return valList[0]