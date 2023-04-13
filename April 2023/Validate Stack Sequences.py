class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #pushed - stack
        #poped - queue
        stack = []
        for num in pushed:
            stack.append(num)
            # print("a",stack)
            # print(popped[0],stack[-1])
            while(len(popped)>0 and len(stack)>0 and stack[-1]==popped[0]):
                stack.pop()
                popped.pop(0)
                # print(stack,popped)
            # print("b",stack)
        if(len(stack)==0):
            return True
        else:
            return False
