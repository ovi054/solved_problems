class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = Counter(s)
        n = len(s)

        if(n<k):
            return False

        remaining = 0
        for _, value in counter.items():
            remaining+= value%2
        if remaining<=k:
            return True
        else:
            return False