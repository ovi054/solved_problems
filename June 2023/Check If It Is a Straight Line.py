class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        y2 = coordinates[n-1][1] 
        x2 = coordinates[n-1][0]
        y1 = coordinates[0][1]
        x1 =  coordinates[0][0]
        #slope = (y1 - y2)/ (x1 - x2)
        for coordinate in coordinates:
            x= coordinate[0]
            y =coordinate[1]
            if((y-y1)*(x1 - x2) != (x-x1)*(y1 - y2)):
                return False
        return True