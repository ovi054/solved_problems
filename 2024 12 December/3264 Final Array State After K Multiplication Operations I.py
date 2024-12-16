class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for index, value in enumerate(nums):
            heappush(heap,(value, index))

        for each in range(k):
            value, index = heappop(heap)
            value = value*multiplier
            heappush(heap,(value, index))

        for value, index in heap:
            nums[index] = value

        return nums