class Solution:
    setList = set()
    def __init__(self):
        if not Solution.setList:
            self.precompute()
    def canPartition(self,numStr, target, index, curSum):
        if(index>=len(numStr)):
            return curSum==target

        for i in range(index+1,len(numStr)+1):
            part = int(numStr[index:i])
            if(self.canPartition(numStr, target, i,part+curSum)):
                return True
        return False

    def precompute(self):
        for i in range(1,1001):
            if self.canPartition(str(i*i),i,0,0):
                self.setList.add(i)
    
    def punishmentNumber(self, n: int) -> int:
        # self.setList = {1, 9, 10, 909, 657, 918, 792, 414, 675, 36, 297, 45, 945, 55, 703, 964, 82, 91, 990, 991, 99, 100, 999, 1000, 235, 369, 370, 756, 379}
        out = 0
        for i in range(1,n+1):
            # sq = i*i
            # if(canPartition(str(sq),i,0,0)):
            #     out+=i*i
            if i in self.setList:
                out+=i*i

        return out  