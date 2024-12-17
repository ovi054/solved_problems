class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hashTable = defaultdict(int)

        for each in s:
            hashTable[each]+=1


        heap = []
        for key in hashTable:
            heappush(heap,(-ord(key),hashTable[key]))

        output = ''
        while(heap):
            value, count = heappop(heap)
            if(count>repeatLimit):
                output = output+ repeatLimit*chr(-value)
                if(heap):
                    value2, count2 = heappop(heap)
                    output = output+ chr(-value2)
                    if(count2-1>0):
                        heappush(heap,(value2, count2-1))
                    heappush(heap,(value, count-repeatLimit))
            else:
                output = output + count*chr(-value)

        return output
        