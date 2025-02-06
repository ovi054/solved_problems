class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        n = len(nums)

        hashTable = defaultdict(list)

        for i in range(n):
            for j in range(i+1,n):
                product = nums[i]*nums[j]
                hashTable[product].append([i,j])


        count = 0


        for key in hashTable.keys():
            pair = hashTable[key]
            m = len(pair)

            count += m*(m-1)*4

        return count
