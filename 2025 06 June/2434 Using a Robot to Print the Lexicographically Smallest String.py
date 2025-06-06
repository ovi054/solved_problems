class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        nextClose = [""]*n
        curSmallIndex = n-1
        curSmallVal = "z"
        for i in range(n-1,-1,-1):
            if ord(s[i])<ord(curSmallVal):
                curSmallVal = s[i]
                # curSmallIndex = i
            nextClose[i] = curSmallVal


        t = []
        output = []
        i = 0
        while(i<n):
            # toStr =  nextClose[i]
            # output.append(s[toStr:i-1:-1] if i>0 else s[toStr::-1])
            # i = toStr+1
            t.append(s[i])
            if i+1<n:
                while(t and ord(t[-1])<=ord(nextClose[i+1])):
                    output.append(t.pop(-1))
            i+=1
    
        while(t):
            output.append(t.pop(-1))

        return ''.join(output)  