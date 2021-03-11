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
    # Count(mid)를 통해서 범위에 제일 가운데 값을 기준으로 DVD개수와 비교
    if Count(mid)<=k:
        # res에 mid를 담는다.
        res=mid
        # 오른쪽 기준점을 왼쪽으로 1칸 당긴다.
        rt=mid-1
    # DVD 개수 (k)가 Count(mid) 보다 더 작다면
    else:
        #왼쪽 기준점을 오른쪽으로 1칸 당긴다
        lt=mid+1

print(res)