class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = set()
        columns = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.add(i)
                    columns.add(j)   

        for item in rows:
            for j in range(n):
                matrix[item][j] = 0

        for item in columns:
            for i in range(m):
                matrix[i][item] = 0   