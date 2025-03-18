class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        i = 0
        j = 1
        n = len(nums)
        output = 1
        while(i<n and j<n):
            bit = nums[i]
            while(j<n and bit & nums[j] ==0):
                bit = bit | nums[j]
                j+=1
            output = max(output, j-i)
            i = i+1
            j = i+1
            

        return output
        
        


        