import sys
sys.stdin=open("input.txt","rt")

a=[list(map(int,input().split())) for _ in range(7)]

cnt=0
for i in range(3):
    for j in range(7):
        word=a[j][i:i+5]
        #제일 앞과 제일 뒤 인덱스를 비교
        if word==word[::-1]:
            # 둘이 똑같다면 cnt+1
            cnt+=1
        # 굳이 5개의 인덱스를 다 돌 필요가 없음
        # 반만해서 첫 값과 마지막 값을 비교해서 다르다면, for문 break
        for k in range(2):
            if a[i+k][j]!=a[i+4-k][j]:
                break
        else:
            cnt+=1

print(cnt)

'''
#Tutor's Code
import sys
sys.stdin=open("input.txt", "r")
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
# i는 0,1,2 만 가능하다. 3이상이면 5개를 했을 때, 격자판 밖으로 벗어난다.
for i in range(3):
    for j in range(7):
        # j가 행 / i가 5개씩 분리하기
        tmp=board[j][i:i+5]
        # 거꾸로 만들어 내는 것
        # 가로(행)로 체크
        if tmp==tmp[::-1]:
            cnt+=1
        # 길이가 5개짜리는 0,1,2만 하면 됨
        # 세로(열)를 체크
        for k in range(2):
            #
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        #정상적으로 for문을 종료하면, else문을 탐
        else:
            cnt+=1
            
print(cnt)

'''