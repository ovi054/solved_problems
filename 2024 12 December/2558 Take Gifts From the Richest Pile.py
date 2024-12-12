import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        maxHeap = [-gift for gift in gifts]
        heapq.heapify(maxHeap)

        for i in range(0,k):
            largest = -heapq.heappop(maxHeap)
            sqRoot = math.floor(math.sqrt(largest))
            heapq.heappush(maxHeap, -sqRoot)

        return -sum(maxHeap)  