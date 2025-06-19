class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        output = 0
        curMin = nums[0]

        for i in range(1,len(nums)):
            if nums[i]-curMin>k:
                output+=1
                curMin = nums[i]
        return output+1

        