n=int(input())
a=1000-n
sum=0
while True:
  if a//500>0:
    sum+=a//500
    a=a%500
  elif a//100>0:
    sum+=a//100
    a=a%100
  elif a//50>0:
    sum+=a//50
    a=a%50
  elif a//10>0:
    sum+=a//10
    a=a%10
  elif a//5>0:
    sum+=a//5
    a=a%5
  elif a//1>0:
    sum+=a//1
    a=a%1
  else:
    break
    
print(sum)