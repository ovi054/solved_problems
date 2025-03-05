class Solution:
    def coloredCells(self, n: int) -> int:
        x = n - 1
        if x==0:
            return 1
        else:
            return 1+ (4*(x*(x+1)))//2
        