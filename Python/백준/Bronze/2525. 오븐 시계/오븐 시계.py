h, m = map(int, input().split())
C = int(input())

h += C // 60
m += C % 60

if m>=60:
    h += 1
    print(h%24, m-60)
else:
    print(h%24, m)