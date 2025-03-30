class Solution
    def partitionLabels(self, s str) - List[int]
        hashTable = defaultdict(int)

        for index,char in enumerate(s)
            hashTable[char] = index

        output = []
        i = 0
        n = len(s)
        lastOcc = 0
        count = 0
        prevOcc = -1
        while(in)
            char = s[i]
            lastOcc = max(hashTable[char],lastOcc)
            i+=1
            count+=1
            if count==lastOcc-prevOcc
                output.append(count)
                prevOcc = lastOcc
                count = 0
                lastOcc = lastOcc+1
                i = lastOcc
        return output