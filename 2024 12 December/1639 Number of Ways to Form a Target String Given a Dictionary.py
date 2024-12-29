class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        freqtable ={}

        for i in range(len(words)):
            for j in range(len(words[i])):
                char = words[i][j]
                if char not in freqtable:
                    freqtable[char] = [0]*len(words[i])
                    freqtable[char][j] +=1
                else:
                    freqtable[char][j] +=1

        w = len(words[0])
        t = len(target)

        memo = {}

        def solve(i, j): 
            #i--> target, j--> word
            if (i,j) in memo:
                 return memo[(i,j)]
            if(i>=t):
                return 1
            if(j>=w):
                return 0

            char = target[i]
            freq = freqtable[char][j] if char in freqtable else 0

            taken = freq*solve(i+1, j+1)
            notTaken = solve(i,j+1)

            memo[(i,j)] = notTaken+ taken
            return memo[(i,j)]

        return solve(0,0)%(10**9+7)