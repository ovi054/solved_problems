class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        count = 0
        for i in range(0,n):
            for j in range(n):
                if baskets[j]>=fruits[i]:
                    baskets[j] = 0
                    count+=1
                    break
        return n-count
