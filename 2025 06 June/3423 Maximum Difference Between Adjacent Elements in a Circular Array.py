class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        output = abs(nums[1]-nums[0])
        for i in range(2,len(nums)):
            output = max(output, abs(nums[i]-nums[i-1]))

        return output