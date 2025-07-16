 class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        curA = 1
        oddEven = 0
        curB = 0
        evenOdd = 0
        evenCount = 0
        oddCount = 0
        n = len(nums)

        for i in range(n):
            cur = nums[i]%2
            if cur == 0:
                evenCount += 1
            else:
                oddCount += 1

            if curA!=cur:
                oddEven+=1
                curA = 1 -curA
            if curB!=cur:
                evenOdd+=1
                curB = 1 - curB

        return max(evenOdd, oddEven, evenCount, oddCount)

   