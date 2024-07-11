class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char ==")":
                rev = []
                while stack and stack[-1]!="(":
                    rev += stack.pop(-1)
                stack.pop(-1)
                stack.extend(rev)
            else:
                stack.append(char)
        return ''.join(stack)    