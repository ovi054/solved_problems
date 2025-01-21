class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        prefixSum = []
        # m = len(grid)
        n = len(grid[0])

        prefixUp = [0]
        prefixDown = [0]

        upSum = 0
        downSum = 0
        for i in range(n):
            upSum+=grid[0][i]
            downSum+=grid[1][i]
            prefixUp.append(upSum)
            prefixDown.append(downSum)

        minVal = inf
        for i in range(n):
            topRemaining = upSum - prefixUp[i+1]
            bottomRemaining = prefixDown[i]
            minVal = min(minVal, max(topRemaining,bottomRemaining))

        
        

        return minVal
        
