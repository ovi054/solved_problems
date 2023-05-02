class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # product = 1
        # for each in nums:
        #     product  = product*each
        # if(product>0):
        #     return 1
        # elif(product<0):
        #     return -1
        # else:
        #     return 0
        sign = 1
        for each in nums:
            if(each<0):
                sign = -sign
            elif(each==0):
                return 0
        return sign
        # if(neg%2==0):
        #     return 1
        # else:
        #     return -1