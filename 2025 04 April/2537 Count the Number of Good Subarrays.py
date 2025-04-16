class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        hashTable = defaultdict(int)
        
        i = 0
        j = 0
        n = len(nums)
        pair = 0
        count = 0

        while(i<n and j<n):
            pair+=hashTable[nums[j]]
            hashTable[nums[j]]+=1
            while(pair>=k):
                count+= n - j
                hashTable[nums[i]]-=1
                pair-=hashTable[nums[i]]
                i+=1
            j+=1
        return count