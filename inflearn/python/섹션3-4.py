import sys
sys.stdin=open("input.txt","rt")

n1=int(input())
n1_list=list(map(int,input().split()))

n2=int(input())
n2_list=list(map(int,input().split()))

res=n1_list+n2_list
res.sort()

for i in res:
    print(i, end=" ")


'''
# sort()를 사용하지 않고 작성해보자
# 기존에 작성가능한 코드는 O(n) 인데 이를 O(nlogn)으로 바꿔보자
import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
p1=p2=0
c=[]
# 하나의 포인트가 끝까지 가면 멈춤
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
# p1이 n까지 못가고 남음
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

for x in c:
    print(x, end=" ")

'''