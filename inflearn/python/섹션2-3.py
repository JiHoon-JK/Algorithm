# 파일에서 값을 가져옴
import sys
# 채점을 할 때는 아래 코드 주석 처리
sys.stdin=open("input.txt", "rt")

# n개의 정수와 K번째 큰 값을 가져온다.
n, k =map(int, input().split())
# n개의 리스트를 리스트형식으로 가져온다.
n_list=list(map(int,input().split()))

result=[]

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            result.append(n_list[i]+n_list[j]+n_list[m])

result = list(set(result))
result.sort(reverse=True)

print(result[k-1])

'''
# 파일에서 값을 가져옴
import sys
# 채점을 할 때는 아래 코드 주석 처리
sys.stdin=open("input.txt", "rt")

# n개의 정수와 K번째 큰 값을 가져온다.
n, k =map(int, input().split())
# n개의 리스트를 리스트형식으로 가져온다.
a=list(map(int,input().split()))

res=[]

# 3중 for문 : 주어진 배열에서 3개를 뽑는 경우의 수 구현
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            # 중복을 제거하면 res에 입력
            res.append(a[i]+a[j]+a[m])

# 중복을 제거하는 자료구조 : set()
# res를 list화 시켜서 sort사용(내림차순 정렬)
res=list(set(res))
res.sort(reverse=True)
# k번째 추출
print(res[k-1])
'''