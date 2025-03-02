class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0,n-1):
            if nums[i]==nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0

        output = []
        zeroCount = 0
        for num in nums:
            if num>0:
                output.append(num)
            else:
                zeroCount+=1

        for i in range(zeroCount):
            output.append(0)

        return output