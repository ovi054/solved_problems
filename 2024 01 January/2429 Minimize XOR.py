class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countSetBit(number):
            setBits = bin(number).count('1')
            return setBits
        
        setBitsNum2 = countSetBit(num2)
        setBitsNum1 = countSetBit(num1)


        diff = abs(setBitsNum2 - setBitsNum1)
        num1Bin = list('0'*35+bin(num1)[2:])
        count = 0

        if(setBitsNum1>setBitsNum2):
            for i in range(len(num1Bin)-1, -1, -1):
                if num1Bin[i]=='1':
                    num1Bin[i]='0'
                    count+=1
                if(count==diff):
                    break
        elif(setBitsNum1<setBitsNum2):
            for i in range(len(num1Bin)-1, -1, -1):
                if num1Bin[i]=='0':
                    num1Bin[i]='1'
                    count+=1
                if(count==diff):
                    break
        return int(''.join(num1Bin), 2)

        