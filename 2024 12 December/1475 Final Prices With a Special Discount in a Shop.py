class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for index, value in enumerate(prices):
            while(stack and stack[-1][1]>=value):
                topIndex, topValue = stack.pop(-1)
                prices[topIndex] = topValue - value
            stack.append([index,value])
        return prices