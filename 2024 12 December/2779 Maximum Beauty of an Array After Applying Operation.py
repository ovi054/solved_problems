class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        def findLeastIndex(value):
            start = 0
            end = len(nums) - 1

            resultIndex = len(nums) - 1

            while(start<=end):
                mid = (start+end)//2

                if(nums[mid]>=value):
                    resultIndex = mid
                    end = mid - 1

                elif(nums[mid]<value):
                    start = mid + 1
            return resultIndex

        def findHighestIndex(value):
            start = 0
            end = len(nums) -1 

            resultIndex = 0

            while(start<=end):
                mid = (start+end)//2

                if(nums[mid]<=value):
                    resultIndex = mid
                    start = mid + 1
                elif(nums[mid]>value):
                    end = mid - 1

            return resultIndex


        output = -1
        start = nums[0] - k
        end = nums[n-1] + k

        for value in range(start, end+1):
            leastIndex = findLeastIndex(value-k)
            highestIndex = findHighestIndex(value+k)
            count = highestIndex-leastIndex+1
            output =max(output,count)

        return output