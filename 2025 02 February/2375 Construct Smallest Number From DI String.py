class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        numList = []

        for i in range(1,len(pattern)+2):
            numList.append(i)
        permuts = (sorted(permutations(numList)))
        output = ''
        for permut in permuts:
            followPattern = True
            for i in range(len(pattern)):
                if pattern[i]=='I' and permut[i+1]<permut[i]:
                    followPattern =False
                    continue
                elif pattern[i]=='D' and permut[i+1]>permut[i]:
                    followPattern = False
                    continue
            if followPattern:
                output = ''.join(map(str,permut))
                break

        return output
        