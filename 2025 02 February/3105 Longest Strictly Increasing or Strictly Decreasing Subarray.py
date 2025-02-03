class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        currentInc = 1
        # maxIncLength = 1

        currentDec = 1
        # maxDecLength = 1
        maxLength = 1

        n = len(nums)

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                currentInc+=1
            else:
                currentInc = 1

            # maxIncLength = max(maxIncLength, currentInc)

            if nums[i]<nums[i-1]:
                currentDec+=1
            else:
                currentDec = 1

            # maxDecLength = max(maxDecLength, currentDec)
            maxLength = max(maxLength, currentInc, currentDec)

        return maxLength

        