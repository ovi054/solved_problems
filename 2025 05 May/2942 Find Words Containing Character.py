class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for index, word in enumerate(words):
            if x in word:
                output.append(index)
        return output
        