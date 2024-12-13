class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        selcted = set()
        minHeap = [(val, idx) for idx, val in enumerate(nums)]
        heapify(minHeap)

        def getMinIndex():
            while minHeap and minHeap[0][1] in selcted:
                heappop(minHeap)
            return minHeap[0][1] if minHeap else None

        output = 0
        while(getMinIndex()!=None):
            minValueIndex = getMinIndex()
            heappop(minHeap)
            output += nums[minValueIndex]
            selcted.add(minValueIndex)
            if(minValueIndex<n-1):
                selcted.add(minValueIndex+1)
            if(minValueIndex>0):
                selcted.add(minValueIndex-1)

        return output