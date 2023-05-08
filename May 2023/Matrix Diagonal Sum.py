class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sumValue = 0
        for i in range(0,n):
            value = mat[i][i] + mat[i][n-i-1]
            sumValue += value
        if(n%2!=0):
            sumValue = sumValue - mat[i//2][i//2]
        return sumValue
