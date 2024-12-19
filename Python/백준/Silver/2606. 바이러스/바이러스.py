n=int(input())
m=int(input())
list=[[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    a,b=map(int, input().split())
    list[a].append(b)
    list[b].append(a)

def dfs(m):
    visited[m]=1
    for i in list[m]:
        if visited[i]==0:
            dfs(i)

dfs(1)
print(sum(visited)-1)
