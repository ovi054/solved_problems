class Solution:
    def removeStars(self, s: str) -> str:
        stack =[]
        for each in s:
            if(each=='*'):
                stack.pop()
            else:
                stack.append(each)
        return ''.join(stack)