class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            nextDp = defaultdict(int)
            for curSum, count in dp.items():
                nextDp[curSum+num] += count
                nextDp[curSum-num] += count
            dp = nextDp
        return dp[target]        