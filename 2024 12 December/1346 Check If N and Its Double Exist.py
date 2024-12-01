class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mySet = set()
        for val in arr:
            if val in mySet:
                return True
            else:
                mySet.add(val*2)
                if(val/2==val//2):
                   mySet.add(val//2) 
        return False
        