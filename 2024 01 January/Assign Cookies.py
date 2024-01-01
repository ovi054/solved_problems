class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0
        for i in range(len(g)):
            if len(s)==0:
                break
            for j in range(len(s)):
                if g[i]<=s[j]:
                    s.pop(j)
                    count+=1
                    break
            else:
                break
        return count

        