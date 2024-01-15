class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnerTable = defaultdict(int)
        loserTable = defaultdict(int)

        for a,b in matches:
            winnerTable[a] +=1
            loserTable[b] +=1
        out1,out2 = [],[]
        for key in winnerTable:
            if key not in loserTable:
                out1.append(key)
        for key in loserTable:
            if loserTable[key]==1:
                out2.append(key)
        return [sorted(out1),sorted(out2)]
        