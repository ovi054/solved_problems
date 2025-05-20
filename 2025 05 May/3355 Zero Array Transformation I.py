class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0]*(n+1)

        for a,b in queries:
            diff[a]-=1
            diff[b+1]+=1

        prefix = []
        prefix.append(diff[0])

        for i in range(1,n):
            prefix.append(prefix[i-1]+diff[i])

        for i in range(0,n):
            if nums[i]+prefix[i]>0:
                return False

        return True
        