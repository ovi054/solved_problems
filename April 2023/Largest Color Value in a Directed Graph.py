class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        hashTable = defaultdict(list)
        memo = {}
        indegrees = [0] * n
        outdegrees = [0] * n
        visited  = [0]*n
        for a,b in edges:
            hashTable[a].append(b)
        #     outdegrees[a] += 1
        #     indegrees[b] += 1
        # zero_indegrees = list(i for i in range(n) if indegrees[i] == 0 and outdegrees[i]!=0)
        def mergeDict(x,y):
            z = dict(Counter(x)+Counter(y))
            return z
        def sumDict(x,y):
            z = {}
            for key in x.keys():
                z[key] = x[key]
            for key in y.keys():
                if key in z:
                    z[key] = max(z[key],y[key])
                else:
                    z[key] = y[key]
            return z
        def dfs(node,colorTable):
            mergedFinal = {}
            colorTable[colors[node]] = 1
            if(visited[node]==1):
                return {"cycle":900}
            elif(node in memo):
                visited[node]=1
                # print("yes")
                mergedFinal = memo[node] 
            elif(node not in hashTable):
                visited[node]=1
                mergedFinal = colorTable
            # elif(len(hashTable[node])>1):
            else:
                visited[node]=1
                maxValue = -1
                for adj in hashTable[node]:
                    merged = mergeDict(colorTable,dfs(adj,{}))
                    # # print(merged)
                    # mergedValue = max(merged.values())
                    # if(mergedValue>maxValue):
                    #     maxValue = mergedValue
                    #     mergedFinal = merged
                    mergedFinal = sumDict(mergedFinal,merged)
                    # print(merged,mergedFinal)
            # print(mergedFinal)
            memo[node] = mergedFinal
            visited[node]=2
            return mergedFinal
        output = -1
        for i in range(0,n):
            colorTable = dfs(i,{})
            if('cycle' in colorTable):
                return -1
            if(max(colorTable.values())>output):
                output = max(colorTable.values())
            # visited  = [0]*n
        return output

