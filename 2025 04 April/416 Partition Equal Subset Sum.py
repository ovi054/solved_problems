class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sumValue = sum(nums)
        if sumValue%2!=0:
            return False
        target = sumValue//2
        n = len(nums)

        memo = [[None] * (target + 1) for _ in range(n)]

        def solve(i, remaining):
            if i>=n or remaining<0:
                return False

            if remaining == 0:
                return True

            if memo[i][remaining] is not None:
                return memo[i][remaining]

            include = solve(i+1, remaining-nums[i])
            exclude = solve(i+1, remaining)
            memo[i][remaining] = include or exclude
            return memo[i][remaining]

        if sumValue%2!=0:
            return False
        return solve(0, target)
        