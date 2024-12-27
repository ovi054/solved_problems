class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        output = 0
        stack = []
        n = len(values)
        curVal =values[n-1]-(n-1) 
        stack.append(curVal)
        for i in range(n-2,-1,-1):
            top = stack[-1]
            curVal =values[i]-i 
            output = max(output, top+values[i]+i)
            if(top<curVal):
                stack.pop()
                stack.append(curVal)
        return output
        