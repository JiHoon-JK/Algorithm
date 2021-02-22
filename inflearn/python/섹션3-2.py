###숫자만 추출###
import sys
sys.stdin=open("input.txt","rt")

# res : 문자열에서 숫자를 담을 배열
res=[]
n=list(input())
for i in range(len(n)):
    # isdigit() 을 이용하여, n[i]가 숫자인지 확인 (숫자면 True, 아니면 False)
    if n[i].isdigit():
        res.append(n[i])

# res를 join하고 앞쪽에 0을 제거한다. for문을 돌리기위해서 정수화시킨다. join() / lstrip()
score = int(''.join(res).lstrip("0"))

# divisor : 약수들의 배열
divisor=[]
# 약수는 1부터 시작해서 score까지 반복해야한다.
for j in range(1,score+1):
    if score%j==0:
        divisor.append(j)

print(score)
print(len(divisor))

'''
import sys
sys.stdin=open("input.txt","r")
s=input()
res=0
for x in s:
    # isdigit():문자열에서 숫자형태 찾기 / isdecimal():0~9까지 숫자찾기
    if x.isdecimal():
        #자동적으로 제일 앞 0은 제거된다.
        res=res*10+int(x)
        
cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1

print(cnt)

'''