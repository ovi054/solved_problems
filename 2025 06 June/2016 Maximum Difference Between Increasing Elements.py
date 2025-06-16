class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        output = -1
        curMax = -1
        for i in range(n-1,-1,-1):
            output = max(output, curMax - nums[i]) 
            curMax = max(curMax, nums[i])
        return output if output>0 else -1
