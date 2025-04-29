class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        maxVal = max(nums)

        i = 0
        j = 0
        n = len(nums)
        curCount = 0
        output = 0
        while(i<n and j<n):
            if nums[j]==maxVal:
                curCount+=1
            while(curCount==k):
                output+= n-j

                if nums[i]==maxVal:
                    curCount -= 1

                i+=1
            j+=1
        return output
