class Solution:
    def minimumLength(self, s: str) -> int:

        counter = Counter(s)
        output = 0
        for item, value in counter.items():
            if value%2==0:
                output+=2
            else:
                output+=1

        return output