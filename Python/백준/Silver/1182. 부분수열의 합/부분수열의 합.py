from itertools import combinations


n, s=map(int, input().split())
count=0
arr =list(map(int, input().split()))
for i in range(1, n+1):
    comb = combinations(arr, i)
    for x in comb:
        if sum(x)==s:
            count+=1
print(count)
