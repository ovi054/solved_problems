class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if ord(char)>= ord('0') and ord(char)<= ord('9'):
                if stack:
                    stack.pop(-1)
            else:
                stack.append(char)
                
        return ''.join(stack)