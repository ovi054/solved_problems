class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        def cyclicIncrement(c):
            return chr((ord(c)-ord('a')+1)%26 + ord('a'))

        m, n  = len(str1), len(str2)
        i, j = 0, 0

        while(i<m and j<n):
            if (str1[i]== str2[j] or cyclicIncrement(str1[i])==str2[j]):
                j+=1
            i+=1

        if j==n:
            return True
        else:
            return False
        


        