class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)

        remaining = k* ceil(n/k) - n

        for i in range(remaining):
            s = s+ fill
        output = []
        for i in range(0, n+remaining, k):
            output.append(s[i:i+k])
        
        return output
