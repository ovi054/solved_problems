class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def check(n):
            if n==0:
                return True
            elif n%3==2:
                return False
            else:
                return check(n//3)

        return check(n)