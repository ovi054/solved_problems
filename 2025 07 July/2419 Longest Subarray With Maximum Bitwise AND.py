class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxNum = max(nums)
        i = 0
        output = 1
        while(i<n):
            count = 0
            if nums[i]==maxNum:
                while(i<n and nums[i]==maxNum):
                    count+=1
                    i+=1
                output = max(output, count)
                # i-=1
            else:
                i+=1
            

        return output


        