class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)
        smallest, secondSmallest = 999, 999
        for i in range(0,n):
            if prices[i]<smallest:
                secondSmallest = smallest
                smallest = prices[i]
            elif prices[i]<secondSmallest:
                secondSmallest = prices[i]
        twoChocolatePrice = smallest + secondSmallest
        if(twoChocolatePrice<=money):
            return money - twoChocolatePrice
        else:
            return money

        