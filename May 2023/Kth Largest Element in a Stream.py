class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.size = len(self.nums)

    def add(self, val: int) -> int:
        index = self.binarySearch(val)
        self.nums.insert(index,val)
        self.size += 1
        # print(self.nums)
        # size = len(self.nums)
        return self.nums[self.size-self.k]


    def binarySearch(self, val):
        start = 0
        end = self.size - 1
        while(start<=end):
            mid = (start+end)//2
            if(val==self.nums[mid]):
                return mid
            elif(self.nums[mid]<val):
                start = mid + 1
            else:
                end = mid - 1
        return end + 1

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)