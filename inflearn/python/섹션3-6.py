import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
# 최대값으로 잡을 max 설정
max=0

for i in range(n):
    sum1=0
    sum2=0
    for j in range(n):
        #sum1은 행의 합
        sum1+=a[i][j]
        #sum2는 열의 합
        sum2+=a[j][i]
    if max<sum1:
        max=sum1
    if max<sum2:
        max=sum2

#sum1,sum2 초기화
sum1=sum2=0

for i in range(n):
    # 왼쪽 대각선 합 : sum1
    sum1+=a[i][i]
    # 오른쪽 대각선 합 : sum2
    sum2+=a[i][n-1-i]
    if sum1>max:
        max=sum1
    if sum2>max:
        max=sum2

print(max)

'''
import sys
sys.stdin=open("input.txt","r")
n=int(input())

# map() 코드가 한 줄을 읽음. 이를 리스트화까지 시킨 것
# 이를 n번 해야함. (n바퀴를 돈다)
a=[list(map(int,input().split())) for _ in range(n)]
#행과 열의 합 (최댓값 : largest)
largest=-2147000000
for i in range(n):
    # 행의합 sum1 / 열의합 sum2
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        # sum2의 열이 고정([i])
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
    
# 대각선 합 구하기
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2

print(largest)

'''