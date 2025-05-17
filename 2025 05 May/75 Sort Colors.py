class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashTable = defaultdict(int)

        for num in nums:
            hashTable[num]+=1
        output = []

        index = 0
        for i in range(0,3):
            for j in range(hashTable[i]):
                nums[index] = i
                index+=1

        return nums