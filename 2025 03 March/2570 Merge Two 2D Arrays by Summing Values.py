class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashTable = defaultdict(int)
        for a,b in nums1:
            hashTable[a] = b
        for a, b in nums2:
            hashTable[a] = b+ hashTable[a]

        output = []

        for key, value in hashTable.items():
            output.append([key,value])

        return sorted(output)