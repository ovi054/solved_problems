class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = []
        for i in range(26):
            parent.append(i)

        def union(chx,chy):
            x = ord(chx)-ord('a')
            y = ord(chy)-ord('a')
            rootX = findIn(x)
            rootY = findIn(y)
            if rootX == rootY:
                return
            if rootX<rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY

        def findIn(x):
            if x!= parent[x]:
                return findIn(parent[x])
            else:
                return x

        def find(chx):
            x = ord(chx)-ord('a')
            while x!= parent[x]:
                x = parent[x]
            return chr(x+ord('a'))

        for cha, chb in zip(s1,s2):
            union(cha,chb)

        output = []

        for char in baseStr:
            output.append(find(char))

        return ''.join(output)