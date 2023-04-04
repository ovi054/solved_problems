#tags: Two Pointer
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        # hashTable = defaultdict(list)
        # for i in range(len(people)):
        #     if(people[i] not in hashTable):
        #         hashTable[limit-people[i]].append(i)
        #         # print(hashTable)
        #     else:
        #         value = hashTable[people[i]].pop()
        #         if(len(hashTable[people[i]]))==0:
        #             hashTable.pop(people[i])
        #         people[i] = -1
        #         people[value] = -1
        #         count = count + 1
        people = sorted(people)
        curSum = 0
        i = 0
        j = len(people) -1
        while(i<=j):
            curSum = people[i] + people[j]
            if(i==j):
                count = count +1
                i = i+1
                j = j-1
            elif(curSum<=limit):
                i = i+1
                j = j -1
                count = count +1
            elif(curSum>limit):
                count = count + 1
                j = j - 1
        return count