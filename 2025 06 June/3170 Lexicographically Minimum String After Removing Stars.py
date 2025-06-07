class Solution:
    def clearStars(self, s: str) -> str:
        s= list(s)

        n = len(s)

        heap = []

        for i in range(n):
            if s[i]=='*':
                topVal, topIndex = heappop(heap)
                s[i] = ''
                s[-topIndex] = ''
            else:
                heappush(heap,(s[i],-i))
        return ''.join(s)

        