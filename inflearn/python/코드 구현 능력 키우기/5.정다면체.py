import  sys
sys.stdin=open('input.txt','rt')

n, m=map(int, input().split())
# N,M의 주사위에서 나올 수 있는 숫자의 합을 모은 리스트
sum_list = []
# 정N면체에서 나올 수 있는 수
for i in range(1,n+1):
    # 정M면체에서 나올 수 있는 수
    for j in range(1,m+1):
        sum = i+j
        # 합 리스트에 추가
        sum_list.append(sum)
# sum_list 오름차순 정렬
sum_list.sort()
# sum_cnt 딕셔너리 생성
sum_cnt=dict()

# 해당 딕셔너리의 갯수를 파악해서 key:value형태로 만들기
for k in sum_list:
    if k not in sum_cnt.keys():
        sum_cnt[k]=1
    else:
        sum_cnt[k]+=1

# sum_cnt에서 가장 큰 value 값 찾기
lot_sum_cnt=max(sum_cnt.values())

# 결과 배열 만들기
result=[]
# sum_cnt 딕셔너리에서 가장 큰 value값을 가지는 key값을 result에 추가
for key,value in sum_cnt.items():
    if(value==lot_sum_cnt):
        result.append(key)

# result 리스트를 문자열로 변환해서 하나씩 출력
print(' '.join(map(str,result)))

'''
(Tutor's Code)

import sys
sys.stdin=open("input.txt","r")
n, m=map(int, input().split())
cnt=[0]*(n+m+3)
# max는 가장 작은 값으로 설정
max=-2147000000
for i in range(1, n+1):
    for j in range(1, m+1):
        #눈의 합, 숫자가 나타날 때마다 해당 인덱스에 값이 1씩 추가
        cnt[i+j]+=1 
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i]=max:
        # 한 칸 띄우고 출력
        print(i, end=" ")
'''