class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        
        visited = []
        for i in range(m):
            visited.append([])
            for j in range(n):
                visited[i].append(0)

        direction = [(-1,0),(1,0),(0,-1),(0,1)]

        def canVisit(i_, j_):
            if i_<0 or i_>=m or j_<0 or j_>=n:
                return False

            if visited[i_][j_]==1:
                return False
            
            return True
            
    

    

        heap = []

        rows = len(heightMap)
        cols = len(heightMap[0])


        top, bottom, left, right = 0, rows - 1, 0, cols - 1

        output = 0

        
        for col in range(left, right + 1):
            heappush(heap, [heightMap[top][col],top, col])
            visited[top][col]=1
        top += 1


        # Traverse the right column (top to bottom)
        for row in range(top, bottom + 1):
            visited[row][right] = 1
            heappush(heap, [heightMap[row][right],row, right])

        right -= 1

        # Traverse the bottom row (right to left)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                visited[bottom][col]=1
                heappush(heap, [heightMap[bottom][col],bottom, col])
                
            bottom -= 1

        # Traverse the left column (bottom to top)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                visited[row][left]=1
                heappush(heap, [heightMap[row][left],row, left])
                
            left += 1


        while(heap):
            height, i ,j = heappop(heap)
            for p,q in direction:
                i_ = i+ p
                j_ = j+q
                if canVisit(i_, j_):
                    height_ = heightMap[i_][j_]
                    output+= max(height-height_,0)
                    # height = height if height<=height_ else height_
                    heappush(heap,[max(height, height_),i_,j_])
                    visited[i_][j_] = 1

        return output