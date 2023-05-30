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



class MyHashSet:

    def __init__(self):
        self.map = []
        self.cap = 1000
        for i in range(self.cap):
            self.map.append([])

    def add(self, key: int) -> None:
        bucket = key % self.cap
        if key not in self.map[bucket]:
            self.map[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % self.cap
        if key in self.map[bucket]:
            self.map[bucket].remove(key)
    def contains(self, key: int) -> bool:
        bucket = key % self.cap
        if key in self.map[bucket]:
            return True
        else:
            return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)