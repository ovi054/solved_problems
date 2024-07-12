#first solution
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


#improved functionality
class Solution:
    def removeSubstring(self, s, subString, addVal):
        first = subString[0]
        second = subString[1]
        stack = []
        output = 0
        for char in s:
            stack.append(char)
            if len(stack)>1 and stack[-2]==first and stack[-1]==second:
                output += addVal
                stack.pop()
                stack.pop()
        return ''.join(stack), output
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if(x>y):
            s, output1 = self.removeSubstring(s,"ab",x)
            s, output2 = self.removeSubstring(s,"ba",y)
        else:
            s, output1 = self.removeSubstring(s,"ba",y)
            s, output2 = self.removeSubstring(s,"ab",x)
        return output1 + output2