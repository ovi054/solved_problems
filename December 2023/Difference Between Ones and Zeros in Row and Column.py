class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        zeroRow = [0]*m
        zeroCol = [0]*n

        # oneRow = [0]*m
        # oneCol = [0]*n

        for i in range(m):
            for j in range(n):
                # if i not in zeroRow:
                #     zeroRow[i] = 0
                # if j not in zeroRow:
                #     zeroRow[j] = 0
                # if i not in zeroCol:
                #     zeroCol[i] = 0
                # if j not in zeroCol:
                #     zeroCol[j] = 0
                # if i not in oneRow:
                #     oneRow[i] = 0
                # if j not in oneRow:
                #     oneRow[j] = 0
                if(grid[i][j]==0):
                    zeroRow[i] += 1
                    zeroCol[j] += 1
                # else:
                #     oneRow[i] += 1
                #     oneCol[j] += 1
        # print(oneRow, oneCol, zeroRow, zeroCol)
        output = []
        for i in range(m):
            output.append([])
            for j in range(n):
                output[i].append(0)
        for i in range(0,m):
            for j in range(0,n):
                output[i][j] = m - zeroRow[i] + n - zeroCol[j] - zeroRow[i] - zeroCol[j]
        return output





        