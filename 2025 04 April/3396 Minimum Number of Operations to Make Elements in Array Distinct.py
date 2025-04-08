class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashTable = {}

        n = len(nums)

        outIndex = -1
        for i in range(n-1,-1,-1):
            if nums[i] not in hashTable:
                hashTable[nums[i]]=1
            else:
                outIndex = i
                break
        return math.ceil((outIndex+1)/3)
        