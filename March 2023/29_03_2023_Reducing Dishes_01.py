#Memo Solution
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction)
        memo = []
        for i in range(0,len(satisfaction)):
            memo.append([])
            for j in range(0,len(satisfaction)):
                memo[i].append(-1)
        def maxSum(satisfaction,i, time):
            if(len(satisfaction)==i):
                return 0
            elif(memo[i][time]!=-1):
                return memo[i][time]
            else:
                f0 = maxSum(satisfaction,i+1,0)
                f1 = maxSum(satisfaction,i+1,time+1)
                value = -1
                if(time==0):
                    value = max(f0,satisfaction[i]*(time+1)+f1)
                else:
                    value = satisfaction[i]*(time+1)+f1
                memo[i][time] = value
                return value
        return maxSum(satisfaction,0,0)