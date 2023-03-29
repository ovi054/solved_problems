#DP solution
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction,reverse=True)
        sumValue = 0
        prefix = 0
        for value in satisfaction:
            prefix = prefix + value
            if prefix<0:
                break
            else:
                sumValue = sumValue + prefix
        return sumValue