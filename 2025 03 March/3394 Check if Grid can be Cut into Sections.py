class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xAxis = []

        for x1, y1, x2, y2 in rectangles:
            xAxis.append([x1,x2])

        xAxis = sorted(xAxis)

        merger = []

        curA = -1
        curB = -1

        curIndex = -1

        for a,b in xAxis:
            if a<curB:
                merger[curIndex][1] = max(curB, b)
                curB = max(curB, b)
                
            else:
                curA = a
                curB = b
                curIndex+=1
                merger.append([a,b])

        if len(merger)>=3:
            return True

        yAxis = []

        for x1, y1, x2, y2 in rectangles:
            yAxis.append([y1,y2])

        yAxis = sorted(yAxis)

        merger = []

        curA = -1
        curB = -1

        curIndex = -1

        for a,b in yAxis:
            if a<curB:
                merger[curIndex][1] = max(curB, b)
                curB = max(curB, b)
                
            else:
                curA = a
                curB = b
                curIndex+=1
                merger.append([a,b])

        if len(merger)>=3:
            return True


        return False
        