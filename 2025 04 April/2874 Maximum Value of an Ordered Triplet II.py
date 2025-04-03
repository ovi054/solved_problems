class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0]*n
        rightMax = [0]*n
        for i in range(n-1):
            leftMax[i+1] = max(nums[i],leftMax[i])
            rightMax[n-i-2] = max(nums[n-i-1], rightMax[n-i-1])

        output = 0
        for i in range(1,n-1):
            output = max(output, (leftMax[i]-nums[i])*rightMax[i])
        return output