#Scramble String - LeetCode 87 -30-03-2023
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        def check(s1,s2):
            n = len(s1)
            if(s1+" "+s2 in memo):
                return memo[s1+" "+s2]
            elif(s1==s2):
                value = True
            elif(n==1):
                value = False
            else:
                value = False
                for i in range(1,n):
                    unswap = check(s1[:i],s2[:i]) and check(s1[i:],s2[i:])
                    swap = check(s1[:i],s2[-i:]) and check(s1[i:],s2[:-i])
                    print(swap)
                    print(unswap)
                    if(swap or unswap):
                        value = True
                        break
            memo[s1+" "+s2] = value
            return value
        return check(s1,s2)
