class Solution:
    def addDigits(self, num: int) -> int:
        if(num<10):
            return num
        else:
            sumValue = 0
            while(num!=0):
                div = num%10
                sumValue = sumValue + div
                num = num//10
            return self.addDigits(sumValue)