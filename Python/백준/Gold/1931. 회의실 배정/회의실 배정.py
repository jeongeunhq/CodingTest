n=int(input())
time=[]

for i in range(n):
    time.append(list(map(int, input().split())))

time=sorted(time, key=lambda x:x[0]) # 시작 시간을 기준으로 정렬
time=sorted(time, key=lambda x:x[1]) # 종료 시간을 기준으로 다시 정렬

ans=1 # 첫 번째 회의는 무조건 선택
end_time=time[0][1] # 첫 번째 회의의 종료 시간을 저장

for i in range(1,n): #두 번째 회의부터 확인
    if end_time<=time[i][0]: # 현재 회의의 시작 시간이 이전 회의의 종료 시간 이후라면
        end_time=time[i][1] # 종료 시간을 갱신
        ans+=1

print(ans)