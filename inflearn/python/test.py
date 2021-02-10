### 파이썬 기초 문법 ###

'''
## 변수 : 데이터들을 저장하는 공간

==================================
영문과 숫자, _로 이루어진다.
대소문자로 시작한다
특수문자를 사용하면 안된다. ($,% 등)
키워드를 사용하면 안된다. (if, for 등)
==================================

a = 1 # 1을 변수a에 대입한다.
A = 2
A1 = 3
#2b = 4  : 변수명은 숫자로 시작하면 안됨
_b = 4
print(a, A, A1, _b)

a, b, c = 3, 2, 1
print(a,b,c)




# 값 교환
a, b = 10, 20
print(a,b)
a, b = b, a
print(a,b)

# 변수 타입
a = 12345  # 정수형
print(type(a))

a = 12.123456 # 실수형 'int'
b = 12.123456798756465423156 # 8바이트 까지만 저장한다. 'float'
print(type(a))
print(b)
a = 'student', "student" # 문자열 'str'
print(a)

'''


'''

## 출력 방식
print("number")
a, b, c = 1, 2, 3
print(a,b,c)
print("number : ",a,b,c)
print(a, b, c,sep=', ') # a를 찍고 , 하고 띄어쓰기!
print(a, b, c, sep='') # a를 찍고 붙여서 b찍고..
print(a, b, c, sep='\n') # a를 찍고 줄바꿈
print(a)
print(b)
print(c)
print(a, end=' ') # a를 찍고 옆으로 한칸
print(b)

'''

'''
## 변수입력과 연산자
a = input("숫자를 입력하세요 : ")
print(a)

a, b = input("숫자를 입력하세요 : ").split() # split() : 분리
print(type(a)) #string형
print(a + b) # a와 b는 문자형이기 때문에 + 연산자로는 그냥 붙이는 것

a, b = input("숫자를 입력하세요 : ").split()
a = int(a) # a를 인트형으로 바꿈
b = int(b) # b를 인트형으로 바꿈
print(a+b) # a+b 연산이 이루어짐

# map : 내장함수
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b) # 더하기 연산
print(a-b) # 빼기 연산
print(a*b) # 곱하기 연산
print(a/b) # 나누기 연산
print(a//b) # 몫 연산
print(a%b) # 나머지 연산
print(a**b) # a를 b번 곱함. 거듭제곱 연산


a=4.3
b=5
c=a+b
print(type(c)) # 실수형과 정수형을 더하면 실수형 결과가 나옴

and or not (논리연산자)
== (관계연산자)

'''

'''
조건문 if (분기, 중첩)

x=7 # = 은 대입연산자
if x==7: # == 은 관계연산자
    print("Lucky!") # 스페이스로 4칸
    print("ㅋㅋ")

if x!=7: # 조건문 성립x
    print('Lucky')

# 중첩 if문
x=15
if x>=10:
    if x%2==1:
        print("10이상의 홀수")

x=10
if x>0:
    if x<10:
        print("10보다 작은 자연수")

x=7
if x>0 and x<10: # and : 교집합 / or : 합집합
    print("10보다 작은 자연수")

x=7
if 0<x<10: # and : 교집합 / or : 합집합
    print("10보다 작은 자연수")

# 분기문
x=10
if x>0:
    print("양수입니다.")
else:
    print("음수입니다.")

# 다중 if문 (if/elif/else)
x=93
# 첫 if문에서 걸리면 밑에 코드는 작동x
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('F')

# if문으로 3개가 구성되면, 개별적으로 작동
if x>=90:
    print('A')
if x>=80:
    print('B')
if x>=70:
    print('C')

'''
'''
반복문 (for, while)

a=range(10) #range():순차적으로 정수 리스트를 만든다.
print(list(a))

a=range(1,11) #range(): 1~10까지 리스트를 만든다.
print(list(a))

for i in range(10): # 0~9까지 10번을 반복하면서 print를 실행한다.
    print(i)

for i in range(10,0,-1): # 10부터 1까지인데, 작아지는 것이기 때문에 -1 을 추가해줘야한다.
    print(i)
i=1
while i<=10: # while문
    print(i)
    i=i+1

i=10
while i>=1:
    print(i)
    i=i-1

i=1
while True: # 무한반복
    print(i)
    if i==10:
        break # i가 10일때, 반복문이 멈춰버린다.
    i+=1 # i=i+1 / 축약연산자

i=1
while i<=10: # 무한반복
    print(i)
    if i==5:
        break # i가 10일때, 반복문이 멈춰버린다.
    i+=1 # i=i+1 / 축약연산자

for i in range(1,11):
    if i%2==0: #i가 짝수인 경우
        continue # continue 밑에 있는 for문의 코드는 그냥 지나가버림
    print(i)

# break로 인한 비정상적인 종료 => else 구문 작동 x
for i in range(1,11):
    print(i)
    if i==5:
        break # 정상적인 종료가 되지않음. (break를 통해서 종료)
else: #for / else 구문도 있음
    # for~else 구문은 정상적으로 종료되어야 실행됨 (break를 했을 때, else구문은 동작하지 않음)
    print(11)


# 정상적으로 for문을 종료 => else 구문 작동 o
for i in range(1,11):
    print(i)
    if i>=15:
        break # 정상적인 종료가 되지않음. (break를 통해서 종료)
else: #for / else 구문도 있음
    # for~else 구문은 정상적으로 종료되어야 실행됨 (break를 했을 때, else구문은 동작하지 않음)
    print(11)
'''

'''
반복문을 이용한 문제풀이
① 1부터 N까지 홀수출력하기
② 1부터 N까지 합 구하기
③ N의 약수출력하기

# 1번
n=int(input()) # 정수화시켜야함
for i in range(1,n+1):
    if i%2==1:
        print('1부터 N까지의 홀수는 : ',i)

#2번
n=int(input())
sum=0 #합을 의미하는 변수
for i in range(1,n+1):
    sum += i
print('1부터 N까지의 합은 : ',sum)

#3번
n=int(input())
divisor = list()
for i in range(1,n+1):
    if n%i==0:
        divisor.append(i)
print('N의 약수는 : ',divisor)
'''

'''
중첩 반복문 ( 2중 for문 )

for i in range(5): # i가 0~4까지 반복
    for j in range(i+1): # j가 0~4까지 반복
        print("*", end=' ')
    print() # 줄바꿈

for i in range(5):
    for j in range(5-i): # 5-i는 반복문을 돌수록 작아짐
        print("*", end=' ')
    print()
'''

'''
문자열과 내장함수
: upper() / lower() / find() / count() / len() / msg[:2] (슬라이스) / isupper() / islower() / isalpha() / ord() / chr()

msg="It is Time"
print(msg.upper()) # msg를 대문자로 바꿈 / 대문자로 변경하는 문자열 내장함수 : upper()
print(msg.lower()) # msg를 소문자로 바꿈 / 소문자로 변경하는 문자열 내장함수 : lower()
print(msg) # 원본은 그대로 있음
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
# tmp 문자열에서 'T'의 위치를 찾는다. / 해당 문자가 처음발견되는 인덱스를 찾는 문자열 내장함수 : find()
print(tmp.count('T'))
# tmp 문자열에서 'T'가 몇개있는가 / 해당 문자가 몇 개 있는지 찾는 내장함수 : count()
print(msg)
print(msg[:2])
# 문자열 슬라이스 : 0부터 2번 전까지 (0번부터 1번까지) 출력
print(msg[3:5])
# 3번부터 5번 전까지 (3번부터 4번까지) 출력
print(len(msg)) # 공백까지 msg의 갯수
for i in range(len(msg)): # 0부터 9까지 반복
    print(msg[i], end=" ")
print()

for x in msg: #x는 msg의 인덱스 하나하나 접근
    print(x, end=" ")
print()

for x in msg:
    if x.isupper() == True: # isupper() : 해당 문자열이 대문자인지 측정
        print(x, end=' ')
print()

for x in msg:
    if x.islower() == True: # islower() : 해당 문자열이 소문자인지 측정
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha() == True: # isalpha() : 알파벳만 나옴(공백은 나오지 않음)
        print(x, end='')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) # ord() : 아스키넘버를 출력 (A~Z A:65 / Z:90)

tmp='az'
for x in tmp:
    print(ord(x)) # 아스키넘버로 출력 a:97 / z:122

tmp=65
print(chr(tmp)) # 아스키넘버를 대응하는 문자로 출력 65:A

tmp=66
print(chr(tmp)) # 66:B
'''

'''
리스트와 내장함수(1)
: list 만들기 / append() / pop() / insert() / remove() / index() /sum() / max() / min()
: shuffle() / sort() , sort(reverse=True) / clear()

import random as r
# 변수 몇 천개를 만드는 것은 굉장히 불편함 => list 형식으로 일렬로 만드는 것이 더 효율적
a=[] #빈 리스트
#print(a)
b=list() #빈 리스트
#print(b)

a=[1,2,3,4,5]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)

c=a+b # 리스트끼리 더할 수 있음
#print(c)

#리스트 내장함수
print(a)
a.append(6) #append() : 리스트 뒤에 해당 값을 추가
print(a)

a.insert(3,7) # insert() : 특정 인덱스에 해당 값을 추가
print(a)

a.pop() # pop() : 맨 뒤에 값이 없어짐
print(a)
a.pop(3) # pop()에 인덱스 번호를 넘기면, 인덱스에 있는 값이 없어짐
print(a)

a.remove(4) # remove() : 해당 값을 찾아서 제거한다.
print(a)

print(a.index(5)) # index() : 해당 값을 찾아서 해당 값의 인덱스 번호를 가져온다.

a=list(range(1,11))
print(a)
print(sum(a)) # sum() : 해당 리스트의 값을 다 더한다.
print(max(a)) # max() : 해당 리스트에서 가장 큰 값을 찾아준다.
print(min(a)) # min() : 해당 리스트에서 가장 작은 값을 찾아준다.
print(min(7,5)) # 인자들 중에서 최소값을 찾기
print(min(7,3,5))
print(a)
r.shuffle(a) # r은 random / shuffle() : 해당 리스트를 무작위로 섞는다. shuffle은 게임을 만들 때 많이 사용
print(a)
a.sort() #sort() : a를 오름차순으로 정렬
print(a)
a.sort(reverse=True) #sort(reverse=True) : a를 내림차순으로 정렬
print(a)

a.clear() # clear() : 리스트에 있는 값들이 전부 사라짐 / 빈 리스트로 만듬
print(a)
'''

'''
리스트와 내장함수(2)
: [:3] (슬라이싱) / enumerate() : (인덱스, 값) 튜플 형식으로 반환 / all() : 모든 값들이 참이여야 함 / any() : 하나만 참이여도 참

a=[23,12,36,53,19]
print(a[:3]) #0번부터 3번전까지
print(a[1:4]) #1번부터 4번전까지
print(len(a)) # 리스트의 길이를 구하는 len()

for i in range(len(a)): #리스트 값을 하나하나씩 찍어냄
    print(a[i], end=' ')
print()

for x in a: #a라는 리스트의 값을 0번부터 접근
    if x%2==1: #x에서 홀수인 경우
        print(x, end=" ")
print()

for x in enumerate(a): # enumerate() : x가 튜블의 형태로 나온다. (인덱스 번호, 원소값) 형태로 반환
    print(x)

# 일렬로 있는 자료를 묶는 것 : 튜플
b=(1,2,3,4,5)
print(b[0])
# 리스트와 튜플이 다른점
#b[0]=7 #값을 새롭게 할당하고 싶을 때 : 튜플은 에러발생 / 리스트는 가능

b=[1,2,3,4,5]
print(b[0])
b[0]=7
print(b[0]) # 리스트는 값 변경 가능

for x in enumerate(a):
    print(x[0], x[1])
print()

# enumerate() 를 제일 많이 사용하는 경우 (인덱스 위치와 값을 같이 가지고 오는 경우)
for index, value in enumerate(a):
    print(index, value)
print()

# 모두가 참일 때 참 : all()
if all(50>x for x in a): # x값은 a에 하나씩 접근 / x 값을 60과 비교한다 / 모두가 전부 True 라면 / all() : 하나라도 false 면 false 반환
    print('YES')
else:
    print('NO')


# 1개만 참이면 전체적으로 참 : any() => 모두가 거짓일 때 false 반환
if any(15>x for x in a):
    print('YES')
else:
    print('NO')
'''

'''
2차원 리스트 생성과 접근
: [[0]*3 for _ in range(3)] => [[0,0,0],[0,0,0],[0,0,0]]
: 행렬의 형태로 그래프를 그려서 문제를 푸는 것도 좋음

# 1차원 리스트를 만든다.
a=[0]*3 # 3개의 리스트 값이 생김
#print(a)

# 2차원 리스트를 만든다.
b=[[0]*3 for _ in range(3)] # [0]*3 의 코드를 range(3) : 3번 도는 것
print(b)
b[0][1]=1
b[1][1]=2
print(b)

# 2차원 리스트를 표처럼 뽑아본다.
for x in b:
    print(x)

# 대괄호를 제거한 리스트의 하나씩 값을 뽑아온다.
# 2차원 리스트를 하나씩 봅아온다.
for x in b:
    for y in x:
        print(y, end=" ")
    print()
    
'''

'''
함수 만들기

# def : define
# 함수는 항상 메인 스크립트 위쪽에 작성
def add(a,b):
    c=a+b
    print(c)

# 메인 스크립트
add(3,2)
add(5,7)

# 많이 사용하는 코드를 계속 메인 스크립트에서 작성한다면, 코드가 굉장히 길어지고 유지, 관리하기가 어려움
# => 함수가 나타남 (겹쳐지는 부분을 함수로 정의)


# a와 b를 더한 값을 반환
def add(a,b):
    c=a+b
    # 결과물을 반환 (return 사용) / return : 함수를 종료하는 기능, 값을 리턴
    return c

# 메인 스크립트에서 결과를 받아서 호출
x=add(3,2)
print(x)

def add(a,b):
    c=a+b
    d=a-b
    return c,d # 두 개의 값을 반환할 수 있음 (C++은 한 개만 반환가능) / 튜플형태로 반환

# 튜플 형태로 여러개의 값을 리턴할 수 있다.
print(add(3,2))


#리스트에서 소수만 출력해보자

def isPrime(x):
    #1은 제외해야해서, 2부터 x-1까지 반복
    for i in range(2, x):
        # 나눠지는 약수가 있다면
        if x%i==0:
            return False
    #나눠지는 약수가 없다면
    return True

a=[12,13,7,9,19]
for y in a:
    if isPrime(y):
        print(y, end=" ")
'''

'''
람다함수 : '익명의 함수', '람다 표현식' 이라고 부름


def plus_one(x):
    return x+1

print(plus_one(1))

# 람다함수로 바꿔보자
# plus_two : 변수이름 / : 이후 반환하는 값
plus_two = lambda x: x+2
print(plus_two(1))

# 람다함수는 왜 사용할까?
# 내장함수의 인자로 사용할 때 굉장히 좋다.
def plus_one(x):
    return x+1

a=[1,2,3]
# plus_one이라는 함수를 실행하고 인수로는 a를 사용한다.   / map(함수명, 인자명)
print(list(map(plus_one, a)))
# output : [2,3,4]

# 함수를 따로 적지않고, print하면서 바로 만들어서 실행
# lambda를 사용해서 익명함수를 만들고, a를 넣어서 사용한다.
# 함수의 이름도 필요가 없다.
print(list(map(lambda x:x+1,a)))

# sort의 인자값으로 lambda를 많이 사용한다.
'''