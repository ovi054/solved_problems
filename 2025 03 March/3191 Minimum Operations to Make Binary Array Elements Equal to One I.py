class Solution:
    def minOperations(self, nums: List[int]) -> int:

        i = 0
        j = 0
        n = len(nums)
        count = 0
        while(i<n-2):
            if nums[i]==0:
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                count+=1
            i+=1
        if nums[n-1]==0 or nums[n-2]==0 or nums[n-3]==0:
            return -1

        return count
