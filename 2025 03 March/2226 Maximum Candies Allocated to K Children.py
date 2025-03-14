class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        candies = sorted(candies)
        n = len(candies)
        def check(val):
            count= 0
            for i in range(n-1,-1,-1):
                count+=  candies[i]//val
                if count>=k:
                    return True
            return False

        result = 0

        start = 1
        end = max(candies)

        while(start<=end):
            mid = (start+end)//2

            if check(mid):
                result = mid
                start = mid+1
            else:
                end = mid-1

        return result