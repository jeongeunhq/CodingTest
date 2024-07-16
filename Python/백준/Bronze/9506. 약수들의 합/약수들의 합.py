
while(1):
  a=int(input())
  if a==-1:
    break
  ls=[]
  for i in range(1,a):
    if a%i==0:
      ls.append(i)
  if sum(ls)==a:
     print(a, " = ", " + ".join(str(i) for i in ls), sep="")
  else:
    print(a,"is NOT perfect.")