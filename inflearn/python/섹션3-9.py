import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

m=[[0]*(n+2) for _ in range(n+2)]
# [0] 값을 가장자리에 모두 둘렀음
for x in range(n):
    for y in range(n):
        if x<n+2 and y<n+2:
            m[x+1][y+1]=a[x][y]

res=0

# 상하좌우 비교하는 로직
for x in range(n+2):
    for y in range(n+2):
        if 0<x<n+1 and 0<y<n+1:
            # 자기자신을 제외한 max_num
            max_num=max(m[x][y-1],m[x][y+1],m[x-1][y],m[x+1][y])
            # 자기 자신이 상하좌우 값의 최댓값보다 크다면
            if m[x][y]>max_num:
                res+=1

print(res)

'''
# Tutor's Code
import sys
sys.stdin=open("input.txt", "r")
# (i,j)로 이루어진 2차원 배열에서 (i-1,j) = 왼쪽 값, (i,j+1) = 아래쪽 값, (i+1,j) = 오른쪽 값, (i,j-1) = 위쪽 값 
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
# 0번 행에 [0]으로 이루어진 n개의 리스트를 넣는다.
a.insert(0,[0]*n)
# 맨 마지막 행에 [0]으로 이루어진 n개의 리스트를 넣는다.
a.append([0]*n)
for x in a:
    # 제일 앞에다가 0을 넣어주기
    x.insert(0,0)
    # 제일 뒤에다가 0을 넣어주기
    x.append(0)
cnt=0
# 제일 처음은 돌지 않아도 됨
for i in range(1, n+1):
    for j in range(1, n+1):
        # i+dx[k] : 행 / j+dy[k] : 열
        # 이 조건이 모두 참이여야 if문을 탈 수 있음 (해당 조건을 4번 하는 것)
        if all(a[i][j]>a[i+dx[k][j+dy[k]] for k in range(4)):
            cnt+=1
            
print(cnt)


'''