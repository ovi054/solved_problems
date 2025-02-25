class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum = [0]
        curSum = 0
        for num in arr:
            curSum+=num
            prefixSum.append(curSum)

        output = 0
        n = len(prefixSum)

        # for i in range(1,n):
        #     for j in range(i):
        #         if (prefixSum[i]-prefixSum[j])%2!=0:
        #             output+=1

        evenCount = 0
        oddCount = 0
        for i in range(n):
            if prefixSum[i]%2==0:
                evenCount+=1
                output+=oddCount
            else:
                oddCount+=1
                output+=evenCount
        return output%1000000007