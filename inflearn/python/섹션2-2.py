# 파일에서 값을 가져옴
import sys
# 채점을 할 때는 아래 코드 주석 처리
sys.stdin=open("input.txt", "rt")

# Case의 갯수
Case=int(input())

for i in range(Case):
    # input.txt의 두 번째 줄을 map()을 통해서 가져와서 split()으로 나눠서 N,s,e,k에 배정한다.
    N, s, e, k=map(int, input().split())
    # input.txt의 세 번째 줄을 list형식으로 가져온다.
    give_list=list(map(int, input().split()))

    # 주어진 리스트를 인덱싱한다.
    sorted_list=give_list[s-1:e]
    #  sort() 오름차순을 한다.
    sorted_list.sort()
    # 오름차순 정렬된 리스트의 k번째 값을 가져온다. (인덱스 기준, k-1)
    result = sorted_list[k-1]

    # 출력 형식에 맞춰서 출력한다.
    print("#%d %d" %(i+1, result))


'''
import sys
sys.stdin=open("input.txt","rt")

# 케이스 갯수
T=int(input())
for t in range(T):
    n, s, e, k=map(int,input().split())
    a=list(map(int, input().split()))
    print(a)

    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))

'''