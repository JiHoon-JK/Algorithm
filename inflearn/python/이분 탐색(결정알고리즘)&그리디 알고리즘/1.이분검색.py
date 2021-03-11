'''
#이분 검색#
1. 이분 검색을 위해서는 무조건 오름차순/내림차순으로 리스트를 정렬해야한다.
2. 처음에 lt(제일 왼쪽 인덱스 값), rt(제일 오른쪽 인덱스 값)를 설정한다.
3. 해당 리스트의 인덱스에서 가운데 값을 mid로 설정한다. ((lt+rt)//2)
4. 반복문을 통해서 리스트의 [mid] 값이 같은지 파악한다.
5. 다르다면, 경우에 따라서 lt와 rt의 값을 변경하면서 범위를 좁힌다.
6. 리스트의 [mid]값이 찾으려는 값과 같다면 반복문을 종료한다.
'''
import sys
sys.stdin=open("input.txt","rt")

# n : 리스트의 갯수  , m : 찾아야하는 수
n, m = map(int,input().split())
a = list(map(int,input().split()))
# 오름차순으로 정렬
a.sort()
# lt : 제일 왼쪽 인덱스 번호 , rt : 제일 오른쪽 인덱스 번호
lt=0
rt=n-1

for i in range(n):
    # mid : 가운데 인덱스 번호
    mid = (lt + rt)//2
    # 중간값이 m과 같을 때
    if a[mid]==m:
        # 인덱스에 +1를 해야 몇번째인지 계산할 수 있다.
        print(mid+1)
        # for문 중단
        break
    # 중간값이 m보다 클 때
    elif a[mid] > m:
        rt=mid-1
    # 중간값이 m보다 작을 때
    else:
        lt=mid+1

'''
# Tutor's Code
import sys
sys.stdin=open("input.txt", "r")
n, m = map(int,input().split())
a=list(map(int, input().split()))
a.sort()
lt=0
rt=n-1
# lt 값이 rt보다 작거나 같다면
while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1

'''


