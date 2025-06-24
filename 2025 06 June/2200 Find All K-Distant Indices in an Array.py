class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        setList = set()

        keys= []
        n = len(nums)
        for i in range(n):
            if nums[i]==key:
                keys.append(nums[i])
                for j in range(-k, k+1):
                    if i+j>=0 and i+j<n:
                        setList.add(i+j)
        return list(setList)
        