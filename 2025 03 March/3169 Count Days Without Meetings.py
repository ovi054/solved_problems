class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        dummy = defaultdict(int)

        for p,q in meetings:
            dummy[p]+=1
            dummy[q+1]-=1
        prefixSum = 0
        count = 0
        
        # for i in range(1,days+1):
        #     curSum = curSum+dummy[i]
        #     if curSum==0:
        #         count+=1

        prevDay = 0

        for i in sorted(dummy.keys()):
            if i>days:
                break

            if prefixSum==0:
                count = count+ i-prevDay-1
            
            if prefixSum+dummy[i]==0:
                count+=1

            prevDay = i
            prefixSum += dummy[i]

        if prefixSum==0:
            count += days-prevDay

        return count