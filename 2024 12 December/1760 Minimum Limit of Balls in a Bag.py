class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def isPossible(value):
            maxOps = 0
            for num in nums:
                ops = num//value
                if(num%value==0):
                    ops-=1 
                maxOps = maxOps + ops
            return maxOps<=maxOperations

        start = 1
        end = max(nums)
        result = end
        while(start<=end):
            print(start, end)
            mid = (start+end)//2
            if(isPossible(mid)):
                result = min(mid, result)
                end = mid - 1
            else:
                start = mid + 1
        return result