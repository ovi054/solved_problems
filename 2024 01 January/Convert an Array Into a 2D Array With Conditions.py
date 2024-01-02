class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        hashTable = defaultdict(int)
        hashTable2 = defaultdict(list)
        output = []
        for i in range(0,n):
            hashTable[nums[i]] += 1
        for key in hashTable:
            for j in range(hashTable[key]):
                hashTable2[j].append(key)
        for key in hashTable2:
            output.append(hashTable2[key])
        return output