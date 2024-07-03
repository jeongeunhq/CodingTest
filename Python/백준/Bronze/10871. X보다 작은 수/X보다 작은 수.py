n, x=input().split()
n=int(n)
x=int(x)
num_list = list(map(int, input().split()))
for i in num_list:
    if i<x:
        print(i)