class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        hashTable = defaultdict(int)

        for char in s:
            hashTable[char]+=1

        while(t>0):
            hashTable2 = defaultdict(int)

            for key in hashTable:
                if key=='z':
                    continue
                else:
                    newKey = chr(ord(key)+1)
                    hashTable2[newKey] = hashTable[key]
            hashTable2['a']+=hashTable['z']
            hashTable2['b']+=hashTable['z']
            hashTable = hashTable2
            t-=1
        
        output = 0
        for key in hashTable:
            output += hashTable[key]

        return output % 1000000007