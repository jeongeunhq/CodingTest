H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)

'''
현재 시간이라고 해서 현재 시간 구해서 작성했는데 런타임 오류 발생
import datetime as dt
hour=dt.datetime.now().hour;
minute=dt.datetime.now().minute;
print(hour,minute);
c = int(input().strip())

if c<60:
    print(hour,minute+c);

elif 60 <= c <= 1000:
  print(hour+int(c/60),minute+(c%60));
'''
