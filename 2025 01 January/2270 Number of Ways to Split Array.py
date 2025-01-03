class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        prefixSum = []
        sumValue = 0
        for num in nums:
            prefixSum.append(sumValue)
            sumValue += num
        prefixSum.append(sumValue)

        n = len(prefixSum)
        totalSum = sumValue
        output = 0
        for i in range(1, n-1):
            if prefixSum[i]>=(totalSum - prefixSum[i]):
                output+=1

        return output  