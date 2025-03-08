class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        curWhite = 0

        for i in range(k):
            if blocks[i]=='W':
                curWhite+=1

        output = curWhite
        i = 0
        j = k
        while(i<n and j<n):
            curWhite += (int(blocks[j]=='W')- int(blocks[i]=='W'))
            # curBlack += (int(blocks[j]=='B')- int(blocks[i]=='B'))
            curOutput = curWhite


            if curOutput<output:
                output = curOutput

            i+=1
            j+=1

        return output
        