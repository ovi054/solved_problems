class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hashTable = defaultdict(int)
        for word2 in words2:
            counter2 = Counter(word2)
            for char, count in counter2.items():
                if hashTable[char]<count:
                    hashTable[char] = count

        def isSubset(counter):
            for key, count in hashTable.items():
                if counter[key]<count:
                    return False
            return True

        output = []

        for word in words1:
            counter = Counter(word)
            if isSubset(counter):
                output.append(word)

        return output        