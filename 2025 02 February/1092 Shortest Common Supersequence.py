class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        m = len(str1)
        n = len(str2)

        #solving without memo

        # def solve(i, j):
        #     if i>=m:
        #         return n-j, str2[j:]
        #     elif j>=n:
        #         return m-i, str1[i:]
        #     if str1[i]==str2[j]:
        #         length, strOut = solve(i+1,j+1)
        #         return length+1, str1[i]+strOut

        #     else:
        #         lengthPickI, strOutPickI = solve(i+1,j)
        #         lengthPickJ, strOutPickJ = solve(i,j+1)
        #         if lengthPickI<lengthPickJ:
        #             return lengthPickI+1, str1[i]+strOutPickI
        #         else:
        #             return lengthPickJ+1, str2[j]+strOutPickJ

        #solving with memo

        # memo = {}

        # def solve(i, j):
        #     if (i,j) in memo:
        #         return memo[(i,j)][0], memo[(i,j)][1]
        #     elif i>=m:
        #         memo[(i,j)] = (n-j, str2[j:])
        #     elif j>=n:
        #         memo[(i,j)] = (m-i, str1[i:])

        #     elif str1[i]==str2[j]:
        #         length, strOut = solve(i+1,j+1)
        #         memo[(i,j)] = (length+1, str1[i]+strOut)

        #     else:
        #         lengthPickI, strOutPickI = solve(i+1,j)
        #         lengthPickJ, strOutPickJ = solve(i,j+1)
        #         if lengthPickI<lengthPickJ:
        #             memo[(i,j)] = (lengthPickI+1, str1[i]+strOutPickI)
        #         else:
        #             memo[(i,j)] = (lengthPickJ+1, str2[j]+strOutPickJ)
            
        #     return memo[(i,j)][0], memo[(i,j)][1]

        #solving with top down coding style

        # memo = {}

        # def solve(i, j):
        #     if (i,j) in memo:
        #         return memo[(i,j)][0], memo[(i,j)][1]
        #     elif i==0:
        #         memo[(i,j)] = (j, str2[:j])
        #     elif j==0:
        #         memo[(i,j)] = (i, str1[:i])

        #     elif str1[i-1]==str2[j-1]:
        #         length, strOut = solve(i-1,j-1)
        #         memo[(i,j)] = (length+1, str1[i-1]+strOut)

        #     else:
        #         lengthPickI, strOutPickI = solve(i-1,j)
        #         lengthPickJ, strOutPickJ = solve(i,j-1)
        #         if lengthPickI<lengthPickJ:
        #             memo[(i,j)] = (lengthPickI+1, str1[i-1]+strOutPickI)
        #         else:
        #             memo[(i,j)] = (lengthPickJ+1, str2[j-1]+strOutPickJ)
            
        #     return memo[(i,j)][0], memo[(i,j)][1]


        memo = []
        for i in range(m+1):
            memo.append([])
            for j in range(n+1):
                memo[i].append(-1)

        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    memo[i][j] = j
                elif j==0:
                    memo[i][j] = i

                elif str1[i-1]==str2[j-1]:
                    length = memo[i-1][j-1]
                    memo[i][j] = length+1

                else:
                    lengthPickI = memo[i-1][j]
                    lengthPickJ = memo[i][j-1]

                    if lengthPickI<lengthPickJ:
                        memo[i][j] = lengthPickI+1
                    else:
                        memo[i][j] = lengthPickJ+1

        # output = memo[m][n][1]
        i= m
        j = n
        output = ''
        while(i>0 or j>0):

            if i==0:
                output+=str2[j-1]
                j-=1
            elif j==0:
                output+=str1[i-1]
                i-=1
            elif str1[i-1]==str2[j-1]:
                output+= str1[i-1]
                i-=1
                j-=1

            elif memo[i-1][j]<memo[i][j-1]:
                output+=str1[i-1]
                i-=1
            else:
                output+=str2[j-1]
                j-=1
            
        output = output[::-1]
        return output