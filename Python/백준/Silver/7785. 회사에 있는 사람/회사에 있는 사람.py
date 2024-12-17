n=int(input())
temp={}
for _ in range(n):
    a,b=input().split()
    temp[a]=b
    if b=='leave':
        del temp[a]

for a in sorted(temp, reverse=True):
    print(a)