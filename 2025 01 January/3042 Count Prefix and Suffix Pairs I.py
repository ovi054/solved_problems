class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for index1, word1 in enumerate(words):
            for index2, word2 in enumerate(words):

                if index1< index2 and word2.startswith(word1) and word2.endswith(word1):
                    count+=1
        return count