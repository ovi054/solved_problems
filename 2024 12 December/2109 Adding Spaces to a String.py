class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = []
        start = 0
        for value in spaces:
            word = s[start:value]
            output.append(word)
            start = value
        word = s[start:len(s)]
        output.append(word)
        return ' '.join(output)    