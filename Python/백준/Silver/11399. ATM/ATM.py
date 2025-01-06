n=int(input())
sum=0
arr=list(map(int, input().split()))
arr.sort()
for i in range(n):
    for j in range(0,i+1):
        sum+=arr[j]
print(sum)