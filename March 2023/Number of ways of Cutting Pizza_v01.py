class Solution:
    memo = {}
    def ways(self, pizza: List[str], k: int) -> int:
        global totalWays
        totalWays = 0
        def findWays(pizza,k,cut):
            global totalWays
            if(k==1):
                return 1
            elif(cut==k-2):
                curWays = 0
                # if(tuple(pizza) in self.memo):
                #     curWays = self.memo[tuple(pizza)]
                # else:
                for i in range(1,len(pizza)):
                    left, right = False, False
                    for j in range(0,i):
                        if('A' in pizza[j]):
                            left = True
                            break
                    for j in range(i,len(pizza)):
                        if('A' in pizza[j]):
                            right = True
                            break
                    if(left and right):
                        curWays = curWays + 1
                for k in range(1,len(pizza[0])):
                    left, right =False, False
                    for i in range(0,len(pizza)):
                        for j in range(0,k):
                            if(pizza[i][j]=='A'):
                                left = True
                                break
                        for j in range(k,len(pizza[0])):
                            if(pizza[i][j]=='A'):
                                right = True
                                break
                    if(left and right):
                        curWays = curWays + 1
                    # self.memo[tuple(pizza)] = curWays
                print(pizza,":", curWays)
                totalWays = totalWays + curWays
            # elif(cut<k-2):
            else:
                for i in range(1,len(pizza)):
                    left, right = False, False
                    for j in range(0,i):
                        if('A' in pizza[j]):
                            left = True
                            break
                    for j in range(i,len(pizza)):
                        if('A' in pizza[j]):
                            right = True
                    if(left and right):
                        findWays(pizza[i:],k,cut+1)
                for m in range(1,len(pizza[0])):
                    left, right =False, False
                    for i in range(0,len(pizza)):
                        for j in range(0,m):
                            if(pizza[i][j]=='A'):
                                left = True
                                break
                        for j in range(m,len(pizza[0])):
                            if(pizza[i][j]=='A'):
                                right = True
                                break
                    newPizza = []
                    if(left and right):
                        for row in pizza:
                            newPizza.append(row[m:])
                        findWays(newPizza,k,cut+1)
            return totalWays
        return findWays(pizza,k,0)
        
                        


