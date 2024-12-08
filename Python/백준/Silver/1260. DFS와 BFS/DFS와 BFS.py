n, m, v = map(int, input().split())

#행렬 생성->0으로 초기화하고 연결 정점 반영
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)


#깊이 우선 탐색
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in range(1, len(graph[v])):
    if graph[v][i] == 1 and not visited[i]:
      dfs(graph, i, visited)


#너비 우선 탐색
def bfs(graph, v, visited):
  queue = [v]
  visited[v] = True
  while queue:
    v = queue.pop(0)
    print(v, end=' ')
    for i in range(1, len(graph[v])):
      if graph[v][i] == 1 and not visited[i]:
        queue.append(i)
        visited[i] = True


dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
