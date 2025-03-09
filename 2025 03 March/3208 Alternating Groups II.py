class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        colors.extend(colors[:k-1])

        i = 0
        j = 1
        N = len(colors)
        output = 0
        while(j<N):
            if colors[j] == colors[j-1]:
                i = j
                j += 1
                continue
            if j-i+1==k:
                output+=1
                i+=1

            j+=1

        return output
        