class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n, maxValue, value = len(gain), 0, 0
        for i in range(0,n):
            value = value + gain[i]
            if(value>maxValue):
                maxValue = value
        return maxValue
