class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        sumValue = sum(derived)

        if(sumValue%2==0):
            return True
        else:
            return False
        