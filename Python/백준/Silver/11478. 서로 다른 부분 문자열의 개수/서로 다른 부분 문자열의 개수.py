a=input()
sum=set()
for i in range(len(a)):
  for j in range(i,len(a)):
    sum.add(a[i:j+1])
print(len(sum))