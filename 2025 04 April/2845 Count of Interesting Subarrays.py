class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        prefix = [0]
        curSum = 0
        for i in range(len(nums)):
            if(nums[i])%modulo==k:
                curSum+=1
            prefix.append(curSum)

        output = 0
        hashTable = defaultdict(int)
        hashTable[0] = 1
        for i in range(1,len(prefix)):
            target = (prefix[i]-k)%modulo
            output+=hashTable[target]
            hashTable[prefix[i]%modulo]+=1
        return output
        