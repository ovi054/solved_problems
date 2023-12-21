class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xValueList = []
        m = len(points)
        for i in range(m):
            xValueList.append(points[i][0])
        xValueList = sorted(xValueList)
        maxDistance = -99999
        for i in range(1,m):
            distance = xValueList[i] - xValueList[i-1]
            if distance>maxDistance:
                maxDistance = distance
        return maxDistance
        