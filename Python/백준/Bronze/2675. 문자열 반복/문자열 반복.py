t=int(input())
for i in range(t):
  a,b=input().split()
  for j in range(len(b)):
    print(int(a)*b[j],end="")
  print()