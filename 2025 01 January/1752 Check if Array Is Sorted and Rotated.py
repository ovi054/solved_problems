class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cutIndex = 0
        for i in range(n-1):
            if nums[i+1]>=nums[i]:
                continue
            else:
                cutIndex = i+1
                break

        result = nums[cutIndex:]+(nums[:cutIndex])

        if result == sorted(result):
            return True

        
        return False
        