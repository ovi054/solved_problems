class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        index = 1
        words  = sentence.split()
        for word in words:
            if word.startswith(searchWord):
                return index
            index+=1
        return -1
                
        