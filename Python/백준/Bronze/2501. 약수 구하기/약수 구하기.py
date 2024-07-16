a,b=map(int,input().split())
ls=[]
for i in range(1,a+1):
  if a%i==0:
    ls.append(i)
if len(ls)<b:
  print(0)
else:
  print(ls[b-1])