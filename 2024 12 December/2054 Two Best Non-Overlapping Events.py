class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        eventList = []
        for start,end,val in events:
            eventList.append((start,1,val))
            eventList.append((end+1,0,val))
        eventList.sort()
        answer = 0
        maxEnd = 0

        for _,isStart, value in eventList:
            if isStart:
                answer = max(answer, maxEnd+value)
            else:
                maxEnd = max(maxEnd,value)
        return answer