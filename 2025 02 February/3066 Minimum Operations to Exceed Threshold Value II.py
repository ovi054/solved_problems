class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        output = 0
        while(nums[0]<k):
            a = heappop(nums)
            b = heappop(nums)
            heappush(nums, a*2+b)
            output+=1
        return output
        