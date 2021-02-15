
# 파일에서 값을 가져옴
import sys
# 채점을 할 때는 아래 코드 주석 처리
sys.stdin=open("input.txt", "rt")

# n명의 학생 수
n=input()
# 학생들의 점수를 리스트형식으로 가져온다.
n_list=list(map(int,input().split()))

# 학생들의 평균 점수 / 소수 첫째 자리에서 반올림
average_score=round(sum(n_list)/len(n_list))
min=float('inf')

# 순서가 중요하기 때문에, sort()를 할 수 없음
for idx, x in enumerate(n_list):
    # 평균에서 해당값까지의 거리 : 절댓값 abs()사용
    tmp = abs(x-average_score)
    # 최솟값보다 tmp가 작다면
    if tmp<min:
        min=tmp
        # score에 해당 값을 넣는다.
        score=x
        # res는 해당 순서
        res=idx+1
    # tmp값과 최솟값이 같다면
    elif tmp==min:
        # score값보다 현재 값이 크다면
        if x>score:
            score=x
            res=idx+1
print(average_score, res)


'''
#Tip) 

# 파일에서 값을 가져옴
import sys
# 채점을 할 때는 아래 코드 주석 처리
sys.stdin=open("input.txt", "rt")

# n명의 학생 수
n=int(input())
# 학생들의 점수를 리스트형식으로 가져온다.
a=list(map(int,input().split()))
# round():소수 첫째 짜리에서 반올림
ave=round(sum(a)/n)
# 최솟값으로 설정할 변수와 큰 값을 초기화값으로 입력한다.
min=float('inf')

# idx : 학생 번호 / enumerate(a) : idx에는 인덱스 값을 넣고, x에는 값을 넣는다.
for idx, x in enumerate(a):
    # 평균과 학생의 값과의 거리를 구해야함
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        # 거리가 같을 떄는 큰 점수로 해야함
        score=x
        # 평균과 가장 가까운 점수의 학생의 인덱스 번호 => res
        # idx에 1을 더해야 인덱스번호
        res=idx+1
    # 이전 값(min)과 tmp가 같다면, x(현재값) > score(이전값)이라면, x를 score로 할당하고, idx번호를 변경한다.
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1

print(ave, res)

'''