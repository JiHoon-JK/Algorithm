### 카드 역배치 ###
import sys
sys.stdin=open("input.txt","rt")

# 카드 배열 생성
card_list=list(range(21))

# 반복이 10번 시행됨
for _ in range(10):
    s, e = map(int,input().split())
    for i in range((e-s+1)//2):
        card_list[s+i], card_list[e-i] = card_list[e-i], card_list[s+i]

card_list.pop(0)
for a in card_list:
    print(a, end=" ")

'''
import sys
sys.stdin=open("input.txt","rt")
#a, b=map(int,input().split())
#a와 b가 자리가 바뀜
#a, b=b, a

# 0~20까지의 리스트가 생성됨
a=list(range(21))

# _ : 변수가 없는 것 / 평소에 i를 넣어서 i에 변수를 넣었음 : _를 활용해서 시간을 단축시킬 수 있음
for _ in range(10):
    s, e=map(int,input().split())
    # (e-s)+1 을 하면 배열의 첫 값과 마지막값을 교환하는 과정을 할 수 있음
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

# 제일 앞쪽(0번 인덱스)에 값을 없앤다.  
a.pop(0)
for x in a:
    print(x, end=" ")



'''