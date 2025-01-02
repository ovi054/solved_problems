class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        n =len(words)

        isVowelList = [0]*n

        vowels = ['a','e','i','o','u']

        vowelSet =set(vowels)
        prefixSum = []
        count = 0
        for index, word in enumerate(words):
            prefixSum.append(count)
            if word[0] in vowelSet and word[-1] in vowelSet:
                isVowelList[index] = 1
                count+= 1


        output = []
        for L, R in queries:
            output.append(prefixSum[R]-prefixSum[L] + isVowelList[R])
        
        return output
        