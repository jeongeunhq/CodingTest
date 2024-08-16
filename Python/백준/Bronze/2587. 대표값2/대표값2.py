list=[]
for i in range(5):
  a=int(input())
  list.append(a)

print(int(sum(list)/5))
list.sort()
print(list[2])