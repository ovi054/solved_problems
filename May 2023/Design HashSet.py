class MyHashSet:

    def __init__(self):
        self.hashTable = {}

    def add(self, key: int) -> None:
        self.hashTable[key] = True

    def remove(self, key: int) -> None:
        if key in self.hashTable:
            self.hashTable.pop(key)

    def contains(self, key: int) -> bool:
        if key in self.hashTable:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)