class NumberContainers:

    def __init__(self):
        self.hashTable = defaultdict(SortedDict)
        self.hash = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if self.hash[index]!=0:
            curValue = self.hash[index]
            del self.hashTable[curValue][index]
        self.hash[index] = number
        self.hashTable[number][index]=1
                

    def find(self, number: int) -> int:
        if self.hashTable[number]:
            return next(iter(self.hashTable[number]))
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)