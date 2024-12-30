class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        z = zero
        u = one

        memo = defaultdict(int)

        def solve(l):

            if l in memo:
                print(l)
                return memo[l]


            if(l>high):
                return 0
            if(l==high):
                return 1

            
            zeroTaken = solve(l+z)
            oneTaken = solve(l+u)

            add = 0
            if(l>=low and l<high):
                add = 1

            memo[l] = (add + zeroTaken + oneTaken) % 1000000007
            return memo[l]

        return solve(0)
        