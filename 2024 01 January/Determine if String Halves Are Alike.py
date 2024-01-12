class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowelList = ['a','e','i','o','u','A','E','I','O','U']
        length = len(s)
        n =length//2
        countA = 0
        countB = 0
        for i in range(n):
            if s[i] in vowelList:
                countA+=1
            if s[length-i-1] in vowelList:
                countB+=1
        return countA==countB   