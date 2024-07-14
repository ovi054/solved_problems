class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        n = len(formula)
        i = 0
        while(i<n):
            item = formula[i]
            if item.islower():
                if stack[-1][0].isupper:
                    stack[-1][0] += item
                i += 1
            elif item.isdigit():
                i += 1
                while(i<n and formula[i].isdigit()):
                    item+=formula[i]
                    i += 1
                if(stack[-1][0]!=')'):
                    stack[-1][1] = int(item)
                else:
                    stack.pop()
                    addStack = []
                    while(stack[-1][0]!='('):
                        topA, topB = stack.pop()
                        topB = topB*int(item)
                        addStack.append([topA,topB])
                    stack.pop()
                    stack.extend(addStack)
            else:
                stack.append([item,1])
                i+=1
        hashTable = defaultdict(int)
        for a,b in stack:
            hashTable[a] +=b
        keys = sorted(hashTable.keys())
        output = ""
        for key in keys:
            if(key=='(' or key==')'):
                continue
            elif hashTable[key]==1:
                output += key
            else:
                output += key + str(hashTable[key])
        return output
