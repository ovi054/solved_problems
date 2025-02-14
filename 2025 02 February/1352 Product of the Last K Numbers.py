class ProductOfNumbers:

    def __init__(self):
        # self.array = []
        self.prefix = [1]
        self.n = 0
        

    def add(self, num: int) -> None:
        if num!=0:
            # self.array.append(num)
            lastVal = self.prefix[self.n]
            self.prefix.append(num*lastVal)
            self.n = self.n + 1
        else:
            # self.array = []
            self.prefix = [1]
            self.n = 0

    def getProduct(self, k: int) -> int:
        if self.n == 0 or k>self.n:
            return 0
        lastVal = self.prefix[self.n]
        prefix = self.prefix[self.n-k]
        return lastVal//prefix
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)