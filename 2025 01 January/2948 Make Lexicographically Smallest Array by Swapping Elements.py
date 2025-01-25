class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        helperNums = sorted(nums)
        hashTable = defaultdict(list)
        n = len(nums)
        groundNoMap = defaultdict(int)
        cur = 0
        hashTable[cur].append(helperNums[0])
        groundNoMap[helperNums[0]] = cur
        for i in range(1, n):
            if helperNums[i]-helperNums[i-1]<=limit:
                hashTable[cur].append(helperNums[i])
                groundNoMap[helperNums[i]] = cur
            else:
                cur+=1
                hashTable[cur].append(helperNums[i])
                groundNoMap[helperNums[i]] = cur



        for i in range(n):
            num = nums[i]
            groupNo = groundNoMap[num]
            firstVal = hashTable[groupNo].pop(0)
            nums[i] = firstVal
        return nums