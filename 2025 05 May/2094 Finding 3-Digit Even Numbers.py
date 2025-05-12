class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        outSet = set()
        for num in range(100,1000):
            if num%2!=0:
                continue
            permCount = defaultdict(int)
            for s in str(num):
                permCount[int(s)]+=1
            isValid = True
            for key in permCount:
                if permCount[key]>count[key]:
                    isValid = False
            if isValid:
                outSet.add(num)

        outSet = list(outSet)
        return sorted(outSet)



        