n=int(input())
yes,no=0,0
for i in range(n):
  a=int(input())
  if a==1:
    yes+=1
  else:
    no+=1
if yes>no:
  print("Junhee is cute!")
else:
  print("Junhee is not cute!")
