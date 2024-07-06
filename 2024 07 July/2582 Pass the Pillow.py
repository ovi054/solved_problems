class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        div = time//(n-1)
        mod = time%(n-1)
        if(div%2==0):
            return mod+1
        else:
            return n-mod