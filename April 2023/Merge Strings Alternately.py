class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1), len(word2)
        i = 0
        newStr = ''
        while(i<m or i <n):
            if(i<m):
                newStr = newStr+word1[i]
            if(i<n):
                newStr = newStr+word2[i]
            i += 1
        return newStr