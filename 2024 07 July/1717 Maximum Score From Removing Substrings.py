class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        valList = []
        output = 0
        if(x>y):
            valList.extend(['a','b',x,y])
        else:
            valList.extend(['b','a',y,x])

        for char in s:
            stack.append(char)
            if len(stack)>1 and stack[-2]==valList[0] and stack[-1]==valList[1]:
                output += valList[2]
                stack.pop()
                stack.pop()
        s = ''.join(stack)
        stack = []
        for char in s:
            stack.append(char)
            if len(stack)>1 and stack[-2]==valList[1] and stack[-1]==valList[0]:
                output += valList[3]
                stack.pop()
                stack.pop()
        return output