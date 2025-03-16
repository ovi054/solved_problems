class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks = sorted(ranks)
        def check(val):
            carCount = 0
            for rank in ranks:
                carCount+= int((val//rank)**0.5)
                if carCount>=cars:
                    return True
            return False

        start = 0
        end = max(ranks)*cars*cars
        result = 0
        while(start<=end):
            mid = (start+end)//2
            if check(mid):
                result = mid
                end = mid-1
            else:
                start = mid+1

        return result

        

        
        