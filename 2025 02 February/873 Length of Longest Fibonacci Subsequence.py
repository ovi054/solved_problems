class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # def putNum(a,b, i):
        #     if a==-1 or b==-1:
        #         return True
        #     elif a+b==arr[i]:
        #         return True
        #     else:
        #         return False

        # def solve(i, a, b, count):
        #     if i>=n:
        #         return count
        
        #     out = solve(i+1, a, b, count)
        #     if(putNum(a,b,i)):
        #         out  = max(out, solve(i+1, b, arr[i], count+1))

        #     return out

        hashTable = defaultdict(list)

        for i in range(n):
            hashTable[arr[i]].append(i)


        def helper(a,b,bIndex):
            if (a+b) in hashTable:
                index = bisect.bisect_right(hashTable[a+b], bIndex)
                if index < len(hashTable[a+b]) and bIndex>index:
                    return hashTable[a+b][index]
                else:
                    None

        def solve(a, b, bIndex, count):
            nextIndex= helper(a,b,bIndex)
            if nextIndex:
                return solve(b, a+b, nextIndex, count+1)
            else:
                return count

        output = 2
        for i in range(n-1):
            for j in range(i+1, n):
                output = max(output, solve(arr[i],arr[j], j, 2))

        return output if output>2 else 0