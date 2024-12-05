class Solution:
    def canChange(self, start: str, target: str) -> bool:
        m, n = len(start), len(target)
        startList = []
        positionList = []
        for i in range(m):
            if start[i] != '_':
                startList.append(start[i])
                positionList.append(i)
        m = len(startList)

        if m==0 and start==target:
            return True
        
        i, j = 0, 0
        while i<m and j<n:
            if(target[j]=='L' and startList[i]=='L' and positionList[i]>=j):
                i+=1
                j+=1
            elif(target[j]=='R' and startList[i]=='R' and positionList[i]<=j):
                i+=1
                j+=1
            elif(target[j]=='_'):
                j+=1
            else:
                return False
        while(j<n):
            if(target[j]=='_'):
                j+=1
            else:
                return False
        return i==m and j==n
        