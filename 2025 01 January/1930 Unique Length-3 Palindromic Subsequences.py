class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        setS = set(s)
        output = 0
        for char in setS:
            leftmost = s.find(char)
            rightmost = s.rfind(char)
            count = 0
            if(leftmost!=rightmost):
                newSet = set(s[leftmost+1:rightmost])
                count = len(newSet)
            output+=count

        return output