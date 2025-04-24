class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        setList = set()
        for i in range(n):
            setList.add(nums[i])
        disNum = len(setList)
        i = 0
        j = 0
        count = 0
        output = 0
        hashTable = defaultdict(int)
        while(i<n and j<n):
            if hashTable[nums[j]]==0:
                count+=1
            hashTable[nums[j]]+=1

            while(count==disNum and i<=j):
                output+=(n-j)
                hashTable[nums[i]]-=1
                if hashTable[nums[i]]==0:
                    count-=1
                i+=1
            j+=1

        return output
