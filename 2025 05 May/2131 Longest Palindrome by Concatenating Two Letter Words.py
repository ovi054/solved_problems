class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashTable = defaultdict(int)
        output = 0
        for word in words:
            new = word[1]+word[0]
            if hashTable[new]:
                hashTable[new]-=1
                output+=4
            else:

                hashTable[word]+=1


        for word in hashTable:
            if hashTable[word]>0 and word[0]==word[1]:
                output+=2
                break

        return output
        