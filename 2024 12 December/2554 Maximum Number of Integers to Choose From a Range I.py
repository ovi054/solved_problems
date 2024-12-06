class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        banned = set(banned)
        count = 0
        sumVal = 0
        for i in range(1,n+1):
            if i not in banned:
                if sumVal+i<=maxSum:
                    sumVal = sumVal+i
                    count= count+1
                else:
                    break
        return count