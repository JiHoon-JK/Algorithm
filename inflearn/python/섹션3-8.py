import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    row, way, step=map(int,input().split())
    #왼쪽으로 회전
    if way==0:
        for _ in range(step):
            # a[row-1]행의 0번째 값을 빼고 제일 뒤에 붙인다 = 왼쪽으로 회전
            a[row-1].append(a[row-1].pop(0))
    #오른쪽으로 회전
    else:
        for _ in range(step):
            # a[row-1]행의 마지막 값을 빼고 제일 앞(0번째 인덱스)에 붙인다 = 오른쪽으로 회전
            a[row-1].insert(0,a[row-1].pop())

res=0
s=0
e=n-1

for i in range(n):
    # s부터 e까지 반복
    for j in range(s, e+1):
        res+=a[i][j]
    # 2//n보다 작은 행들을 s를 더하고, e를 빼면서 범위를 좁혀야함.
    # 모래시계 윗부분
    if i<n//2:
        s+=1
        e-=1
    # 2//n 보다 큰 행들은 s를 빼고, e를 더하면서 범위를 늘려야함.
    # 모래시계 아랫부분
    else:
        s-=1
        e+=1

print(res)

'''
#Tutor's Code

import sys
sys.stdin=open("input.txt","r")
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k =map(int,input().split())
    #왼쪽 방향으로 회전
    if t==0:
        for _ in range(k):
            # h행의 첫번째 인덱스를 지운다.
            # 빼낸 값을 제일 뒤에 붙인다.
            # 이를 통해서 1번의 회전이 일어난다.
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            # [h-1]행의 제일 뒤에 있는 값을 0번째로 붙인다.
            a[h-1].insert(0, a[h-1].pop())

#for x in a:
#    print(x)            

# s=0 / e=n-1 
# s는 1이 증가하고, e는 1이 감소해야함.
# 2//n 보다 커지는 열들은, s가 1이 감소하고, e는 1이 증가해야한다.
# 이 과정을 거쳐서 모래시계 형태가 만들어진다.

res=0
s=0
e=n-1
for i in range(n):
    # s부터 e까지 돌기
    for j in range(s, e+1):
        res+=a[i][j]
    # i가 n//2보다 작을 때는 좁혀져야함.
    if i<n//2:
        s+=1
        e-=1
    # i가 n//2보다 클 때는 넓혀져야함.
    else:
        s-=1
        e+=1
print(res)
'''
