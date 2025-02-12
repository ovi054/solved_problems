class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashTable = defaultdict(list)

        def countSumDigits(num):
            strNum = str(num)
            out = 0
            for char in strNum:
                out += (ord(char) - ord('0'))
            return out

        for num in nums:
            key = countSumDigits(num)
            hashTable[key].append(num)
            hashTable[key] = sorted(hashTable[key], reverse=True)[:2]

        output = -1
        for key in hashTable.keys():
            if len(hashTable[key])>=2:
                output  = max(output, sum(hashTable[key]))

        return output