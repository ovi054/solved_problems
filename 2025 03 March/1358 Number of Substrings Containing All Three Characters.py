class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        hashTable = defaultdict(int)
        n = len(s)

        i = 0
        j = 0
        output=0
        while(i<n and j<n):
            hashTable[s[j]]+=1

            if len(hashTable)==3:
                output+= n - j

                hashTable[s[i]]-=1
                if hashTable[s[i]]==0:
                    del hashTable[s[i]]
                hashTable[s[j]]-=1
                if hashTable[s[j]]==0:
                    del hashTable[s[j]]
                i+=1

            else:
                j+=1

        return output
        