class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        sumValue  = sum(nums)
        n = len(nums)
        if sum(nums)==0:
            return 0

        def check(k):
            diff = [0]*n
            for i in range(k):
                l,r, val = queries[i]
                diff[l]-=val
                if r+1<n:
                    diff[r+1]+=val
            cumSum = 0
            for i in range(n):
                cumSum+=diff[i]
                if nums[i]+cumSum>0:
                    return False
            return True
            
            
        result = -1
        start, end = 1, len(queries)
        while(start<=end):
            mid = (start+end)//2
            if check(mid)==True:
                result = mid
                end = mid-1
            else:
                start = mid+1
        return result