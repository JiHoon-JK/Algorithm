import sys
sys.stdin=open("input.txt","rt")

# n은 수열의 갯수 / m은 수열의 총합이 되어야할 수
n, m = map(int,input().split())
n_list=list(map(int,input().split()))

# 합을 통해서 m을 만들었을 경우, cnt+=1
cnt=0

# point:가르키는 부분
point1=0
point2=1

# 더해지는 값 (m과 비교하는 값)
res=n_list[0]

while True:
    if res<m:
        if point2<n:
            res+=n_list[point2]
            point2+=1
        else:
            break
    elif res==m:
        cnt+=1
        res-=n_list[point1]
        point1+=1
    else:
        res-=n_list[point1]
        point1+=1

print(cnt)

'''
import sys
sys.stdin=open("input.txt","rt")
n, m=map(int, input().split())
a=list(map(int,input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        # n개의 수열보다 작을때
        if rt<n:
            tot+=a[rt]
            rt+=1
        # rt가 n이 된 경우 (더 이상의 자료를 더할 것이 없다.)
        else:
            break
    # m과 연속된 수의 합(tot)값이 같을 때
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
        
    # tot값이 m보다 큰 경우
    else:
        tot-=a[lt]
        lt+=1

print(cnt)
'''