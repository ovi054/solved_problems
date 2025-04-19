class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums = sorted(nums)

        left = 0
        right = n-1

        countWithinBounds = 0

        while(left<right):
            if nums[left]+nums[right]<=upper:
                countWithinBounds+=(right-left)
                left+=1
            else:
                right-=1

        countLessBounds = 0
        left = 0
        right = n-1
        while(left<right):
            if nums[left]+nums[right]<lower:
                countLessBounds+=(right-left)
                left+=1
            else:
                right-=1

        return countWithinBounds-countLessBounds
        