def paths(graph,visited,ind):
    visited[ind]=True
    for i in graph[ind]:
        if not visited[visited.index(i)]:
            paths(graph,visited,i)
    
    

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4



graph=[[0 for i in range(n)] for i in range(n)]
visited=[False  for i in range(n)]
graph2=[]
for i in edges:
    graph[i[0]][i[1]]=graph[i[1]][i[0]]=i[2]

for i in range(n):
    ans=[]
    for j in range(n):
        if graph[i][j]!=0:
            ans.append(j)
    graph2.append(ans)    
        


[print(i) for i in graph]
[print(i) for i in graph2]

paths(graph,visited,0)
