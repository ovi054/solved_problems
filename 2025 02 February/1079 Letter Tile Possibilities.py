class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        setList = set()
        def solve(index, s):

            if(index>=len(tiles)):
                if s:
                    setList.add("".join(sorted(s)))
                return
            pick = solve(index+1, s+tiles[index])
            noPick = solve(index+1, s)

        solve(0,'')
        output = 0
        for item in setList:
            n = len(item)
            # if n==0:
            #     continue
            fact = factorial(n)
            counter = Counter(item)
            for _, count in counter.items():
                fact//=factorial(count)
            output+=(fact)
            
        return output
        