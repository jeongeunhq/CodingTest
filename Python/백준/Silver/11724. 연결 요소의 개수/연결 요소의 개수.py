import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
gragh=[[] for _ in range(n+1)]
visited=[0]*(n+1)

def dfs(gragh,v,visited):
    visited[v]=[True]
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh,i,visited)

for i in range(m):
    a,b=map(int,input().split())
    gragh[a].append(b)
    gragh[b].append(a)

count=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(gragh,i,visited)
        count+=1

print(count)