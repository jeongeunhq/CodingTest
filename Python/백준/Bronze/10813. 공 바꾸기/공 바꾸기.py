n, m=map(int, input().split())
list=[]
for i in range(n):
  list.append(i+1)

for _ in range(m):
  i, j=map(int, input().split())
  temp=list[i-1]
  list[i-1]=list[j-1]
  list[j-1]=temp

for i in list:
  print(i,end=' ')