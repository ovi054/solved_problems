class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 =list(s1)
        s2 = list(s2)
        diff = 0
        for i in range(n):
            if s1[i]!=s2[i]:
                diff+=1

        isEqual = True
        # hashTable = defaultdict(int)
        for c1 in s1:
            if c1 not in s2:
                isEqual = False
                break
            else:
                s2.remove(c1)


        # if n<=2:
        #     return diff==0

        return isEqual and diff<=2
        