class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(c):
            if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
                return True
            else:
                return False
        n = len(s)
        curCount = 0
        for i in range(0,k):
            if(isVowel(s[i])):
                curCount += 1
        maxCount = curCount
        for i in range(1,n-k+1):
            if(isVowel(s[i-1])):
                curCount -=1
            if((isVowel(s[i+k-1]))):
                curCount +=1
            if(curCount>maxCount):
                maxCount = curCount
        return maxCount
    
        

