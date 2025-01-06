class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        n = len(boxes)
        prefixList = []
        prefixSum = 0
        prefixCount = 0
        for index,hasBall in enumerate(boxes):
            if hasBall=='1':
                prefixSum+=index
                prefixCount+=1
            prefixList.append((prefixSum,prefixCount))
        postfixList = [(0,0) for i in range(n)]
        postfixSum = 0

        postfixCount = 0
        for i in range(n-1,-1,-1):
            if boxes[i]=='1':
                postfixSum+=i
                postfixCount+=1
            postfixList[i] = (postfixSum, postfixCount)
        output =[0]*n

        for index,hasBall in enumerate(boxes):
            rightCount = prefixCount - prefixList[index][1] 
            rightOutput = prefixSum - prefixList[index][0] - rightCount*index

            leftCount = postfixCount - postfixList[index][1] 
            leftOutput = leftCount*index - (postfixSum - postfixList[index][0])

            output[index] = rightOutput + leftOutput

        return output



        