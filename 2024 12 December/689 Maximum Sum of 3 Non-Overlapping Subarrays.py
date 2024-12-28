class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sumVal = 0
        for i in range(0,k):
            sumVal += nums[i]
        # print(sumVal)

        # heap = []
        sumList = [sumVal]
        # heappush(heap,(-sumVal,0))
        curVal = nums[0]
        i = 1
        n = len(nums)
        while(i<n and i+k-1<n):
            sumVal = sumVal + nums[i+k-1] - curVal
            sumList.append(sumVal)
            curVal = nums[i]
            i+=1
        # print(sumList)
        output = []
        count = 0
        

        memo = {}
        def maxSum(i, count):

            if(i+k>n or count==3):
                return 0
            
            if((i, count) in memo):
                return memo[(i, count)]

            include = sumList[i] + maxSum(i+k,count+1)
            skip = maxSum(i+1,count)
            memo[(i, count)] = max(include,skip)
            return max(include,skip)

        # print(maxSum(0,0))
        # print(sumList[0],maxSum(3,1))

        def solve():
            result = []
            i = 0
            count = 0
            while(count<3 and i+k<=n):
                include = sumList[i] + maxSum(i+k, count+1)
                skip = maxSum(i+1, count)

                if(include>=skip):
                    result.append(i)
                    i+=k
                    count+=1
                else:
                    i+=1
            return result

        return solve()