class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        def checkCollision(a,b):
            if(a=='R' and b=='L'):
                return True
            else:
                False

        # Combine position, dir, and health into a list of lists
        combined = [list(item) for item in zip(positions, healths, directions)]

        # Sort the combined list by the position values
        sorted_combined = sorted(combined, key=lambda x: x[0])

        stack = []
        for item in sorted_combined:
            stack.append(item)
            while(len(stack)>1 and checkCollision(stack[-2][2],stack[-1][2])):
                if(stack[-2][1]==stack[-1][1]):
                    stack.pop()
                    stack.pop()
                elif(stack[-2][1]>stack[-1][1]):
                    stack[-2][1] -= 1
                    stack.pop()
                else:
                    stack[-1][1] -= 1
                    stack.pop(-2)
            
        output = []
        hashTable = {}
        for i,pos,dir in stack:
            hashTable[i] = pos
        for item in positions:
            if item in hashTable:
                output.append(hashTable[item])
        return output     