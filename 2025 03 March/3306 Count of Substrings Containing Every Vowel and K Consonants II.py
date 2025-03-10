class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = {'a','e','i','o','u'}
        nextConsonat = [-1]*n
        curConsIndex = n
        for i in range(n-1,-1,-1):
            nextConsonat[i] = curConsIndex
            if word[i] not in vowels:
                curConsIndex = i

        
        i = 0
        j = 0
        vowelSet = defaultdict(int)
        consCount = 0
        output = 0
        while(i<n and j<n):
            if word[j] in vowels:
                vowelSet[word[j]]+=1
            else:
                consCount+=1

            if consCount>k:
                # vowelSet = defaultdict(int)
                # consCount = 0
                # i+=1
                #moving i to i+1
                if word[i] in vowels:
                    vowelSet[word[i]]-=1
                    if vowelSet[word[i]]==0:
                        del vowelSet[word[i]]
                else:
                    consCount-=1
                if word[j] in vowels:
                    vowelSet[word[j]]-=1
                    if vowelSet[word[j]]==0:
                        del vowelSet[word[j]]
                else:
                    consCount-=1
                i+=1
                # j = j-1
                # j= i

            elif len(vowelSet)==5 and consCount==k:
                output+=nextConsonat[j]-j
                # i+=1
                #moving i to i+1
                if word[i] in vowels:
                    vowelSet[word[i]]-=1
                    if vowelSet[word[i]]==0:
                        del vowelSet[word[i]]
                else:
                    consCount-=1
                if word[j] in vowels:
                    vowelSet[word[j]]-=1
                    if vowelSet[word[j]]==0:
                        del vowelSet[word[j]]
                else:
                    consCount-=1
                i+=1
                # j = j-1
                # j=i
                # vowelSet = defaultdict(int)
                # consCount = 0

            else:
                j+=1

        return output
            


        