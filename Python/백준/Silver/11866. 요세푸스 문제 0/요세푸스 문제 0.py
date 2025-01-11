n, k = map(int, input().split())
count=0
circle=[i+1 for i in range(n)]
arr=[]

for i in range(n):
    count+=k-1
    if count>=len(circle):
        count=count%len(circle)
    arr.append(str(circle.pop(count)) )   
print("<",", ".join(arr),">",sep="")