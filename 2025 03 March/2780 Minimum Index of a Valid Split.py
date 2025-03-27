class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        counter = Counter(nums)

        maxOcc, maxOccCount = counter.most_common(1)[0]

        leftCount, rightCount = 0, maxOccCount

        n = len(nums)

        for i in range(0,n):
            if nums[i]==maxOcc:
                leftCount+=1
                rightCount-=1

            if leftCount>=(i+1)//2+1 and rightCount>=(n-i-1)//2+1:
                return i

        return -1