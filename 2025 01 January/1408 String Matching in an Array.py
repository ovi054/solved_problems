class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        words = sorted(words, key=lambda s: len(s))
        for index1,word1 in enumerate(words):
            for index2 in range(index1+1, len(words)):
                word2 = words[index2] 
                if word1 in word2:
                    output.append(word1)
                    break
        return output