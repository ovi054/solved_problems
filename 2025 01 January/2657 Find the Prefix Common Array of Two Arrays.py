class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()

        n = len(A)
        output = [0]*(n+1)
        for i in range(n):
            a = A[i]
            b = B[i]

            if a==b:
                output[i+1] =output[i]+1

            else:
                setA.add(a)
                setB.add(b)
                count = 0
                toRemove = []
                for element in setA:
                    if element in setB:
                        toRemove.append(element)
                        count+=1
                for each in toRemove:
                    setA.remove(each)
                    setB.remove(each)
                output[i+1] =output[i]+count
        
        output.pop(0)
        return output