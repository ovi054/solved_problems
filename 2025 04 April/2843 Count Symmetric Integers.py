class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0

        for i in range(low, high+1):
            num = str(i)
            length = len(num)
            if len(num)%2==0:
                leftSum = 0
                for m in range(length//2):
                    leftSum+= int(num[m])
                rightSum = 0
                for n in range(length//2, length):
                    rightSum+= int(num[n])
                if leftSum==rightSum:
                    count+=1
        
        return count