class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        def shift_char(char, shift):
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        
        n = len(s)
        diff = [0]*(n+1)

        for start, end, direction in shifts:
            if direction:
                diff[start]+=1
                diff[end+1]-=1
            else:
                diff[start]-=1
                diff[end+1]+=1

        prefix = []
        sumValue = diff[0]
        prefix.append(sumValue)
        for i in range(1,n):
            sumValue += diff[i]
            prefix.append(sumValue)
        sList = list(s)
        for index, value in enumerate(prefix):
            sList[index] = shift_char(sList[index], value)

        return ''.join(sList)
        