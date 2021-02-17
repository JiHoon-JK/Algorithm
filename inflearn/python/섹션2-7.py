import sys
sys.stdin=open("input.txt","rt")

N=int(input())
# N개의 0으로 이루어진 리스트 생성
res=[0]*(N+1)
divisor_num=0

# 2부터 N까지 반복
for i in range(2,N+1):
    if res[i]==0:
        divisor_num+=1
        # i에서 N+1 까지 i씩 건너뛰어서
        for j in range(i,N+1,i):
            res[j]=1

print(divisor_num)


'''
(Tutor's Code)
인덱스 값이 0이면, "소수"
2의 배수는 인덱스 값을 1로 체크 (4,6,8,10...,20 : 소수x)
3의 배수는 인덱스 값을 1로 체크 (6,9,12,15...: 소수x)
5의 배수는 인덱스 값을 1로 체크 (10,15,20 : 소수x)

import sys
sys.stdin=open("input.txt","rt")
n=int(input())
ch=[0]*(n+1)
cnt=0

for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        # range(strat, end, step) : i에서 시작해서 n+1전까지 i씩 간격을 두고
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)


'''
