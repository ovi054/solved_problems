class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if (n<=4):
            return 0
        else:
            minVal = nums[n-1]-nums[3]
            minVal = min(minVal,nums[n-4] - nums[0])
            minVal= min(minVal,nums[n-3] - nums[1])
            minVal= min(minVal,nums[n-2] -nums[2])
            return minVal
        