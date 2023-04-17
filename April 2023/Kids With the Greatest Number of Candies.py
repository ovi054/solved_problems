class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxValue = max(candies)
        boolList =[]
        for each in candies:
            if(each+extraCandies>=maxValue):
                boolList.append(True)
            else:
                boolList.append(False)
        return boolList
