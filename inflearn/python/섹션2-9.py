import sys
sys.stdin=open("input.txt","rt")

MoneyList=[]

n=int(input())
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a, b, c =map(int,tmp)
    # a,b,c 모두 같음
    if a==b and b==c:
        money = 10000 + (a * 1000)
        MoneyList.append(money)
    elif a==b and b!=c:
        money = 1000 + (a*100)
        MoneyList.append(money)
    elif a!=b and b==c:
        money = 1000 + (b*100)
        MoneyList.append(money)
    elif a==c and b!=c:
        money = 1000 + (c*100)
        MoneyList.append(money)
    # a,b,c 모두 다름
    else:
        money = c*100
        MoneyList.append(money)

# MoneyList 를 sort() 사용해서 정렬
MoneyList.sort()
# 제일 큰 값을 호출
print(MoneyList[-1])

'''
#(Tutor's Code)

import sys
sys.stdin=open("input.txt","rt")

res=0
n=int(input())
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a, b, c =map(int,tmp)
    # 첫 if문은 가장 큰 조건을 거는것이 좋음 (제일 좋은 것을/상금이 높은것을 위쪽에 걸기)
    if a==b and b==c:
        money=10000+(a*1000)
    # 계산할 때 한 변수를 잡고 계산을 해야하기 때문에 하나의 값으로 이루어진 조건이 좋음
    elif a=b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    
    # res보다 크면 res에 배정 (반복문을 통해서 res에는 제일 큰 값이 나오게 됨)
    if money>res:
        res=money
 
 print(res)       
        
'''
