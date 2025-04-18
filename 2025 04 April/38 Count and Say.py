class Solution:
    def countAndSay(self, n: int) -> str:

        def say(num):
            m = len(num)
            count = 1

            i = 0
            out = ""
            while(i<m):
                j = i
                while(j<m and num[i]==num[j]):
                    j+=1
                count = j-i
                out += str(count)+num[i]
                i = j
            return out

        finalOut = "1"
        for i in range(1,n):
            finalOut = say(finalOut)
        return finalOut