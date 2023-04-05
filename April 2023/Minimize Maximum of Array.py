class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sumValue = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            sumValue = sumValue + nums[i] 
            avg = math.ceil(sumValue/(i+1))
            if(avg>result):
                result = avg
        return result