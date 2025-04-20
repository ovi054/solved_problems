class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashTable = defaultdict(int)
        zeroCount = 0
        for answer in answers:
            if answer==0:
                zeroCount+=1
            else:
                hashTable[answer]+=1
        output = 0
        for each in hashTable:
            group = hashTable[each]//(each+1)
            if hashTable[each]%(each+1)!=0:
                group+=1
            output+= group*(each+1)
        
        return output+zeroCount
        