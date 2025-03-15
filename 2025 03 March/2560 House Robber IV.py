class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sNums = sorted(nums)
        def check(val):
            i = 0
            house = 0
            while(i<n):
                if nums[i]<=val:
                    house+=1
                    i+=2
                else:
                    i+=1
                if house>=k:
                    return True
            return False

        start = 0
        end = n-1
        result = 0
        while(start<=end):
            mid = (start+end)//2
            if check(sNums[mid]):
                result = sNums[mid]
                end = mid - 1
            else:
                start = mid + 1

        return result