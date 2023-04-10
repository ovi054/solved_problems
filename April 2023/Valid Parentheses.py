class Solution:
    def isValid(self, s: str) -> bool:
        hashTable = {}
        hashTable[')'] = '('
        hashTable[']'] = '['
        hashTable['}'] = '{'
        stack = []
        for each in s:
            if each not in hashTable:
                stack.append(each)
            else:
                if(len(stack)>0 and stack[-1]==hashTable[each]):
                    stack.pop(-1)
                else:
                    return False
        if(len(stack)>0):
            return False
        else:
            return True
        