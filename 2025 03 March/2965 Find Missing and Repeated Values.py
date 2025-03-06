class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        setA = set()
        setB = set()
        for i in range(1,(n*n)+1):
            setA.add(i)
        output = [-1,-1]
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in setB:
                    setB.add(grid[i][j])
                else:
                    output[0] = grid[i][j]
                setA.discard(grid[i][j])
        output[1] = list(setA)[0]
        return output