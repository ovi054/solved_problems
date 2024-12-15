class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculateGain(p,t):
            gain = ((p+1)/(t+1)) - (p/t) 
            return gain
        heap = []

        for p,t in classes:
            gain = calculateGain(p,t)
            heappush(heap,(-gain,p,t))

        for each in range(extraStudents):
            gain, p,t = heappop(heap)
            newGain = calculateGain(p+1,t+1)
            heappush(heap,(-newGain,p+1,t+1))
        sumValue = 0
        for _,p,t in heap:
            sumValue+= p/t
        return sumValue/len(classes)