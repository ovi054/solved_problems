class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        nums = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums.append(grid[i][j])

        nums = sorted(nums)
        target = nums[len(nums)//2]

        result = 0

        for num in nums:
            if (abs(target-num))%x==0:
                result+=(abs(target-num))//x
            else:
                return -1
            

        return result
        