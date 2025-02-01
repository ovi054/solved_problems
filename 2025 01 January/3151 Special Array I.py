class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        i = nums[0]%2

        for num in nums:
            if num%2!=i:
                return False
            
            i = 1 - i
        return True
        