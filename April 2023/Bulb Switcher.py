#only perfect square has odd no of divisor
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # output = 0
        # for i in range(1,n+1):
        #     count = 0
        #     for j in range(1,i+1):
        #         if(i%j == 0):
        #             count += 1
        #     if(count%2!=0):
        #         output += 1
        # return output
        return int(math.sqrt(n))