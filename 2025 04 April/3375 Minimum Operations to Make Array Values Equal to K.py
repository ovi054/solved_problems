class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        hashTable = defaultdict(int)

        for num in nums:
            if num<k:
                return -1
            hashTable[num]+=1

        output = 0

        for key in hashTable.keys():
            if key>k:
                output+=1
        
        return output
        