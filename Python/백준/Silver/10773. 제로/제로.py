n=int(input())
list=[]
for i in range(n):
  a=int(input())
  if a==0:
    list.pop()
  else:
    list.append(a)
print(sum(list))
  