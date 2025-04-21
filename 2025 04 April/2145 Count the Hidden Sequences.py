class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        hidden = [0]
        i = 0
        for diff in differences:
            val = hidden[i]+diff
            hidden.append(val)
            i+=1


        minVal, maxVal = min(hidden), max(hidden)

        rangeL, rangeU = lower-minVal, upper-maxVal

        if rangeU-rangeL+1>0:
            return rangeU-rangeL+1
        else:
            return 0