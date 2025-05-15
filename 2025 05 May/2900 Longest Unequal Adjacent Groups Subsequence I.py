class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        curGroup = -1
        output = []
        for word, group in zip(words, groups):
            if group!=curGroup:
                curGroup = group
                output.append(word)
        return output