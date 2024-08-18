n,p=map(int,input().split())
list=[]
for i in range(n):
  a=int(input())
  list.append(a)
list.sort(reverse=True)

answer=0

for i in list:
  if p>=i:
    q=p//i
    answer+=q
    p%=i 
    if p<=0:
      break
print(answer)