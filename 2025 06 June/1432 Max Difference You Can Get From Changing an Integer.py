class Solution:
    def maxDiff(self, num: int) -> int:
        maxNum = num
        minNum = num

        strNum = str(num)

        for x in range(0,10):
            for y in range(0,10):
                genNum = ''
                for j in range(len(strNum)):
                    if strNum[j]==str(x):
                        genNum += str(y)
                    else:
                        genNum += strNum[j]
                if int(genNum)>maxNum:
                    maxNum = int(genNum)
                if int(genNum)<minNum and len(str(int(genNum)))==len(strNum) and int(genNum)!=0:
                    minNum = int(genNum)
        return maxNum - minNum