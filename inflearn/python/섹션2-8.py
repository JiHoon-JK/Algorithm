import sys
sys.stdin=open('input.txt','rt')

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True

n=int(input())
k=list(map(int,input().split()))
for x in k:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")


'''
(Tutor's Code)

import sys
sys.stdin=open('input.txt','rt')
def reverse(x):
    res=0
	# x가 0이 될때까지 반복
    while x>0:
		# 10으로 나눈 나머지 : t
        t=x%10
        res=res*10+t
        # 10으로 나눈 몫 : x
        x=x//10
	# x를 뒤집은 res를 반환
    return res
    
def isPrime(x):
    # x로 1이 넘어오게 되면 제외시켜야함
    if x==1:
        return false
    # 굳이 x를 다 돌 필요가 없음. 어차피 약수를 찾는 것이기 때문에 x의 절반만 수행 : x//2
    for i in range(2,x//2+1):
        # 약수가 있는 경우
        if x%i==0:
            return false
    # return 당하지 않고 정상적으로 for문이 종료되었다면 else구문 시작
    else:
        return True
n=int(input())
a=list(map(int, input().split()))
for x in a:
    # x를 뒤집은 리스트 : tmp
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")


'''