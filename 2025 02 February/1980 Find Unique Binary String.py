class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        pdt = product("01", repeat = n) 
        setList = set(nums)
        for p in pdt:
            pStr = ''.join(p)
            if pStr not in setList:
                return pStr
        return ''
        