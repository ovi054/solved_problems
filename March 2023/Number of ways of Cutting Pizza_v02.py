class Solution:
    #memo = {}
    
    def ways(self, pizza: List[str], k: int) -> int:
        memo =[]
        for i in range(0,len(pizza)):
            memo.append([])
            for j in range(0,len(pizza[0])):
                memo[i].append([])
                for t in range(0,k):
                    memo[i][j].append(-1)
        def check(pizza,stratRow,endRow,startCol, endCol):
          value =  False
          for i in range(stratRow,endRow):
            for j in range(startCol,endCol):
              if pizza[i][j]=='A':
                value = True
                break
          return value
        # totalWays = 0
        def findWays(pizza,startRow,startCol,k,cut):
            # global totalWays
            result = -1
            if(k==1):
                result = 1
            elif(memo[startRow][startCol][cut] != -1):
                # print("yes")
                result = memo[startRow][startCol][cut]
            elif(cut==k-1):
                result = 1
            else:
                tsum = 0
                for i in range(startRow+1,len(pizza)):
                    left, right = False, False
                    left = check(pizza,startRow,i,startCol,len(pizza[0]))
                    right = check(pizza,i,len(pizza),startCol,len(pizza[0]))
                    # print(left,right)
                    if(left and right):
                        curWays = findWays(pizza,i,startCol,k,cut+1)
                        tsum = tsum + curWays
                        # print(curWays,totalWays)
                for m in range(startCol+1,len(pizza[0])):
                    left, right =False, False
                    left = check(pizza,startRow,len(pizza),startCol,m)
                    right = check(pizza,startRow,len(pizza),m,len(pizza[0]))
                    # print(left,right)
                    if(left and right):
                        curWays = findWays(pizza,startRow,m,k,cut+1)
                        tsum = tsum + curWays
                result =  tsum

            # tempMemo = {}
            # tempMemo[cut] = result
            #print(cut)
            memo[startRow][startCol][cut] = result
            return result
        return findWays(pizza,0,0,k,0)%1000000007