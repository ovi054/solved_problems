class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        charList = [0]*26
        for i in range(n):
            for j in range(len(words[i])):
                charList[ord(words[i][j])-ord('a')] += 1
        for i in range(len(charList)):
            if(charList[i]/n != charList[i]//n):
                return False
        return True