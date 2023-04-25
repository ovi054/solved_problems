class SmallestInfiniteSet:

    def __init__(self):
        self.myList = []
        for i in range(1,1001):
            self.myList.append(i)
    def popSmallest(self) -> int:
        return self.myList.pop(0)

    def addBack(self, num: int) -> None:
        if(self.binarySearch(num)==False):
            bisect.insort_left(self.myList,num)
    
    def binarySearch(self, target):
        start = 0
        end = len(self.myList) - 1
        while(start<=end):
            mid  = (start+end)//2
            if(self.myList[mid]==target):
                return True
            elif(target<self.myList[mid]):
                end = mid - 1
            else:
                start = mid + 1
        return False

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)