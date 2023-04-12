class Solution:
    def simplifyPath(self, path: str) -> str:
        stack =[]
        l = path.split("/")
        # print(l)
        for each in l:
            if(each==''):
                continue
            elif(each=='.'):
                continue
            elif(each=='..'):
                if(len(stack)>0):
                    stack.pop()
                continue
            stack.append(each)
        output = '/' + '/'.join(stack)
        return output
        