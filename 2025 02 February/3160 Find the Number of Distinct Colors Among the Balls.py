class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        hashTable = defaultdict(int)
        
        curColor = defaultdict(int)
        
        output= []
        count = 0
        for x,y in queries:
            if curColor[x] != y:
                z = curColor[x]
                if hashTable[z]>0:
                    hashTable[z] -= 1
                    if hashTable[z] == 0:
                        count -=1
                curColor[x] = y
                if hashTable[y] == 0:
                    count +=1
                hashTable[y]+=1
            
            output.append(count)
                
        #print(curColor) 
        return output