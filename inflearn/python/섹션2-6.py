import sys
sys.stdin=open("input.txt","rt")

# n은 다음 줄의 자연수의 갯수
n=input()
# n개의 자연수들을 리스트에 담기 : n_list
n_list=list(map(int, input().split()))
# 자연수들의 자릿수 합을 저장할 리스트
result=[]

def digit_sum(x):
    # n_list를 하나씩 꺼내서 자릿수마다 더한 다음 result 리스트에 넣기
    for i in range(len(x)):
        result.append(sum(map(int, str(x[i]))))

    # result에서 가장 큰 값
    max_result=max(result)

    # result를 for문으로 돌려서 가장 큰 값일 때 index를 찾기
    for j in range(len(result)):
        # 가장 큰 값과 같을 때 출력
        if result[j]==max_result:
            print(x[j])
            # 겹치는 것도 제일 앞쪽에 있는 값을 먼저 출력하기 때문에 굳이 출력을 더 할 필요없음 break 사용
        break

digit_sum(n_list)

'''
(Tutor's Code)
### 정수형 처리 방법(몫과 나머지 활용) ###
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
def digit_sum(x):
    sum=0
    while x>0:
        # x를 10으로 나눈 나머지를 sum에 추가
        sum+=x%10
        # x를 계속해서 10으로 나눈 몫
        x=x//10
    return sum

# 임의의 가장 작은 값을 배정
max=-2147000000
for x in a:
    # x라는 리스트의 각 자릿수의 합을 구하는 함수 사용
    tot=digit_sum(x)
    if tot>max:
        max=tot
        # 가장 큰 값이 res에 배정
        res=x
print(res)

------------------------------------------------
### 문자형 처리 방법 ###
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum

# 임의의 가장 작은 값을 배정
max=-2147000000
for x in a:
    # x라는 리스트의 각 자릿수의 합을 구하는 함수 사용
    tot=digit_sum(x)
    if tot>max:
        max=tot
        # 가장 큰 값이 res에 배정
        res=x
print(res)

'''