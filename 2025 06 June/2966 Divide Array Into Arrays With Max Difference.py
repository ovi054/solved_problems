class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)

        output = []
        temp = []

        for i in range(len(nums)):
            temp.append(nums[i])
            if len(temp)==3:
                if temp[2]-temp[0]>k or temp[2]-temp[1]>k:
                    return []
                output.append(temp)
                temp = []
        return output
        