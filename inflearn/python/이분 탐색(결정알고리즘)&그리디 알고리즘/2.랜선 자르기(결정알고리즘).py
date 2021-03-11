import sys
sys.stdin=open("input.txt","r")

#자른 랜선의 길이 수를 모두 구한 합을 구하는 함수 Count()
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    # 모든 랜선들을 자른 몫들을 다 더한 cnt를 반환한다.
    return cnt

n, k = map(int,input().split())
# 랜선 길이 배열
Line=[]
# 최대 길이 res
res=0
# 가장 긴 랜선의 길이
largest=0

# Line에 하나씩 넣고, 그 중에서 가장 큰 값을 largest라고 정의
for i in range(n):
    tmp=int(input())
    Line.append(tmp)
    # 둘 중에서 큰 값을 largest에 넣기
    largest=max(largest,tmp)

# 범위는 (1~가장 큰 값) 으로 정해야한다.
lt=1
rt=largest

# rt가 lt보다 크고 같다면 반복문 계속 실행
while lt<=rt:
    # 범위 내에서 가운데 값을 설정
    mid=(lt+rt)//2
    # 총 자른 랜선의 길이 합 Count(mid)
    # 중간 값으로 몫(개수)을 구한 값이 k보다 크거나 같다면 조건 참
    if Count(mid)>=k:
        res=mid
        # 제일 긴 길이를 찾아야하기 때문에 lt값 변경
        lt=mid+1
    # 자른 랜선의 수가 적음
    else:
        rt=mid-1

#해당 반복문을 계속해서 실행해서 최대 길이 값을 구해서 출력한다.
print(res)


