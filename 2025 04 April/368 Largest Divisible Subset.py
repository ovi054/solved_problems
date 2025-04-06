class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        output = []
        
        dp = [1]*n
        maxLength = 1
        prevIndex = [-1]*n
        lastChosen = 0
        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j]+1
                        prevIndex[i] = j

                    if dp[i]>maxLength:
                        maxLength = dp[i]
                        lastChosen = i

        while(lastChosen!=-1):
            output.append(nums[lastChosen])
            lastChosen = prevIndex[lastChosen]
        return output