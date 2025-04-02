class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    result = (nums[i]-nums[j])*nums[k]
                    output = max(result, output)
        return output