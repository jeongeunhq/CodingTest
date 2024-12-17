import sys
import heapq
#연산의 개수
n = int(sys.stdin.readline())
heap=[]
for i in range(n):
    #자연수 x 입력 받기
    x=int(sys.stdin.readline())
    #x가 0이 아닌 경우
    if x!=0:
        #힙에 x를 입력 넣기
        heapq.heappush(heap,x)
    #x가 0인 경우
    else:
        #힙에 아무것도 없는 경우
        if len(heap)!=0:
            #힙에서 가장 작은 값 출력
            print(heapq.heappop(heap))
        #힙에 값이 있는 경우
        else:
            print(0)