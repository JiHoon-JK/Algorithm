import sys
sys.stdin=open("input.txt","rt")

# 문제 갯수
n=int(input())
n_list=list(map(int,input().split()))

# 총 점수를 담을 변수 설정
score=0
count=0

for i in range(n):
    # 정답을 맞춘 경우 : 1
    if n_list[i]==1:
        # count가 1이상이라면, 이전 값이 정답이었다.
        if count>=1:
            count+=1
            score+=count
        # 이번 값은 정답이었지만, 이전 값은 정답이 아니었다.
        else:
            count+=1
            score+=1

    # 정답을 못 맞춘 경우 : 0
    else:
        count=0
        score+=0


print(score)

'''
import sys
sys.stdin=open("input.txt","rt")
n=int(input())
a=list(map(int,input().split()))

sum=0
cnt=0

for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
        
print(sum)
'''