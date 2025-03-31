class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        sumValue = 0
        dummy = []
        n = len(weights)
        for i in range(1,n):
            dummy.append(weights[i]+weights[i-1])

        dummy = sorted(dummy)

        l = n-1

        minValue = 0
        maxValue = 0

        for i in range(k-1):
            minValue+=dummy[i]
            maxValue+= dummy[l-1-i]

        return maxValue-minValue