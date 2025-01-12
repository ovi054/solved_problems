class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        n = len(s)
        if n%2!=0:
            return False
        openStr = []
        openColseStr = []

        for i in range(0,n):
            if locked[i]=='0':
                openColseStr.append(i)
            else:
                if s[i]=='(':
                    openStr.append(i)
                else:
                    if openStr:
                        openStr.pop()
                    elif openColseStr:
                        openColseStr.pop()
                    else:
                        return False
        
        while(openStr and openColseStr and openStr[-1]<openColseStr[-1]):
            openStr.pop()
            openColseStr.pop()
        if openStr:
            return False
        else:
            return True


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        n = len(s)
        if n%2!=0:
            return False
        

        openCount = 0

        for i, j in zip(s, locked):
            if i=='(' or j=='0':
                openCount+=1
            else:
                openCount-=1
            if openCount<0:
                return False

        colseCount = 0

        for i in range(n-1,-1,-1):
            if s[i]==')' or locked[i]=='0':
                colseCount+=1
            else:
                colseCount-=1
            if colseCount<0:
                return False
        
        return True

        