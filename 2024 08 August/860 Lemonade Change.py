class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if(bill==5):
                five+=1
            elif(bill==10):
                five-=1
                if(five<0):
                    return False
                ten+=1
            else:
                if(ten>0 and five>0):
                    ten-=1
                    five-=1
                else:
                    five-=3
                    if(five<0):
                        return False

        return True
        