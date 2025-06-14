class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxNum = num
        minNum =  num

        strNum = str(num)
        for i in range(0,10):
            genMaxNum = 0
            genMinNum = 0
            for j in range(len(strNum)):
                if strNum[j] == str(i):
                    genMaxNum  =  genMaxNum*10+9
                    genMinNum = genMinNum*10+0
                else:
                    genMaxNum = genMaxNum*10+int(strNum[j])
                    genMinNum = genMinNum*10+int(strNum[j])
            if genMaxNum>maxNum:
                maxNum = genMaxNum
            if genMinNum<minNum:
                minNum = genMinNum

        return maxNum-minNum    