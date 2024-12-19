class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        output = 0
        expectedSum = 0
        runningSum = 0
        for i in range(n):
            expectedSum+=i
            runningSum+=arr[i]
            if runningSum==expectedSum:
                output+=1
        return output