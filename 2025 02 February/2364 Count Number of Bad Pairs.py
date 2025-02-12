class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] - i
            
        counter = Counter(nums)
        total = 0
        
        for item, count in counter.items():
            total += (count*(count-1))//2
            
        return (n*(n-1))//2 - total