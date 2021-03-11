import sys
sys.stdin=open("input.txt","r")

def Count(capacity):
    #DVD 한장이 필요
    cnt=1
    # 현재까지 저장된 용량
    sum=0
    for x in List:
        # 용량초과
        if sum+x>capacity:
            # DVD 갯수 추가
            cnt+=1
            # 새롭게 x로 초기화
            sum=x
        else:
            sum+=x
    return cnt


n, k = map(int,input().split())
# List : 노래 리스트 (각 곡의 시간으로 번호가 적혀있다.)
List=list(map(int,input().split()))
# res : DVD의 최소 용량 크기
res=0
# 범위는 1~sum(List)까지
lt=1
# 모든 노래를 다 합친 것
rt=sum(List)

# lt <= rt 라면 계속해서 반복
while lt <= rt:
    mid=(lt+rt)//2
    #
    if Count(mid)<=k:
        res=mid
        rt=mid-1
    else:
        lt=mid+1

print(res)