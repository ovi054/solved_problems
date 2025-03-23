class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        hashTable = defaultdict(list)

        for u,v, val in roads:
            hashTable[u].append([v,val])
            hashTable[v].append([u,val])

        dist = [math.inf]*n

        visited = [False]*n
        count = [0]*n

        queue = [[0, 0]]

        dist[0] = 0

        count[0] = 1

        visited[0] = True

        while(queue):
            d, top = heappop(queue)

            if d > dist[top]: 
                continue

            for adj,val in hashTable[top]:
                #dist[u] + dist[u,v]< dist[v]
                if dist[top]+val<dist[adj]:
                    dist[adj] = dist[top]+val
                    count[adj] = count[top]
                    heappush(queue,[dist[adj],adj])
                elif dist[top]+val==dist[adj]:
                    count[adj] = count[adj] + count[top]
                    # heappush(queue,[dist[adj],adj])


        return count[n-1]% (1000000007)  