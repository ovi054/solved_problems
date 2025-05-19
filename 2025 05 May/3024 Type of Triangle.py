class Solution:
    def triangleType(self, nums: List[int]) -> str:
        hashTable = defaultdict(int)
        a,b,c = nums[0], nums[1], nums[2]
        if a+b>c and a+c>b and b+c>a:
            hashTable[a]+=1
            hashTable[b]+=1
            hashTable[c]+=1
        else:
            return "none"
        
        if len(hashTable.keys())==1:
            return "equilateral"
        elif len(hashTable.keys())==2:
            return "isosceles"
        else:
            return "scalene"