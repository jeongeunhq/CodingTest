n = int(input()) #설탕 총량 입력 받음.
count = 0 #최종 몇 봉지가 필요한지 기록하는 변수.
while True:
  if(n%5==0): #5kg으로 나누어떨어지는지 확인 
    count += n//5 #몫을 계산하여 5kg 설탕이 몇 봉지 필요한지 더해줌.
    break
  elif(n%5!=0 and n>=3): #5kg으로 나누어 떨어지지 않고 남은 양이 3kg 이상인 경우.
    n-=3 #-3씩 감소시키고
    count+=1 #봉지 수 추가.
  elif(n>0 and n<3): #남은 설탕양이 3kg나 5kg로 계산되지 않을 경우
    count = -1
    break
  else:
    break
print(count)