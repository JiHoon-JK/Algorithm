#풀이(1)

# 파일에서 값을 가져옴
import sys
# 채점을 할 때는 아래 코드 주석 처리
#sys.stdin=open("input.txt", "rt")

# input.txt를 map()을 통해서 가져와서 split()으로 나눠서 N, K에 배정한다.
N, K=map(int, input().split())
divisor_array = []

def divisor(N,K):
    for i in range(1,N+1):
        if N%i==0:
            divisor_array.append(i)
    if len(divisor_array) >= K:
        print(divisor_array[K-1])
    else:
        print(-1)


divisor(N,K)

'''
#풀이(2)

# 파일에서 값을 가져옴
import sys
# 채점을 할 때는 아래 코드 주석 처리
sys.stdin=open("input.txt", "rt")
 
# input.txt를 map()을 통해서 가져와서 split()으로 나눠서 N, K에 배정한다.
N, K=map(int, input().split())
# 약수의 갯수
cnt=0
 
for i in range(1,N+1):
    if N%i==0:
        cnt+=1
    if cnt==K:
        print(i)
        break
# 정상적으로 for문이 끝나면 (break를 당하지 않은 것 = K만큼 cnt가 없음)
else:
    print(-1)
'''