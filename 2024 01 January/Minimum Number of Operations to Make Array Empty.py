class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashTable = defaultdict(int)
        n = len(nums)
        for i in range(0,n):
            hashTable[nums[i]]+=1
        count = 0
        for key in hashTable:
            if(hashTable[key]==1):
                return -1
            else:
                count+=(hashTable[key]+2)//3
        return count
        