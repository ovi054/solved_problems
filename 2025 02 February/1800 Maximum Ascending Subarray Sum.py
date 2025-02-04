class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        curSum = nums[0]
        maxSum = nums[0]
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                curSum += nums[i]
            else:
                curSum = nums[i]

            maxSum = max(maxSum,curSum)

        return maxSum
        