class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        boolMat = []
        m = len(matrix)
        n = len(matrix[0])
        output = []
        top , bottom, left, right = 0,m-1,0,n-1
        count = 0
        size = m*n
        while(count <size):
            for i in range(left, right+1):
                output.append(matrix[top][i])
                count +=1
            top += 1
            for i in range(top, bottom+1):
                output.append(matrix[i][right])
                count +=1
            right -= 1
            if(count <size):
                for i in range(right,left-1,-1):
                    output.append(matrix[bottom][i])
                    count +=1
                bottom -= 1
            if(count<size):
                for i in range(bottom,top-1,-1):
                    output.append(matrix[i][left])
                    count +=1
                left += 1
        return output
