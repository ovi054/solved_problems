class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefixSum = [0]
        curSum = 0

        for num in nums:
            curSum+=num
            prefixSum.append(curSum)

        n = len(prefixSum)
        maxNeg = 0
        maxPos = 0
        output = 0
        for i in range(1,n):
            if prefixSum[i]>0:
                output = max(output, abs(prefixSum[i]-maxNeg))
                maxPos = max(maxPos, prefixSum[i])
            else:
                output = max(output, abs(prefixSum[i]-maxPos))
                maxNeg = min(maxNeg, prefixSum[i])
            
        return output