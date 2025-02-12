class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(s)
        n = len(part)
        stack = []
        partList = list(part)
        
        for i in range(m):
            stack.append(s[i])
            
            if len(stack)>=n:
                
                if stack[-n:]==partList:
                    
                    for i in range(n):
                        stack.pop()
                          
        return ''.join(stack)