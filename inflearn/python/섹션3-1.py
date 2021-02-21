import sys
sys.stdin=open("input.txt","rt")

n=int(input())

for i in range(n):
    string=input().lower()
    if string == string[::-1]:
        check="YES"
    else:
        check="NO"
    print("#%d %s" %(i+1, check))

'''
import sys
sys.stdin=open("input.txt","r")
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    # size를 다 볼 필요가 없음 절반만 보면 된다! 5개일 경우 2번만 비교하면 됨
    for j in range(size//2):
        # ex) level => s[j]=l (앞쪽) , s[-1-j]=l (뒤쪽)
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    # for문을 정상적으로 끝낸다면, else문을 탄다.
    else:
        print("#%d YES" %(i+1))
        
        
import sys
sys.stdin=open("input.txt","r")
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
    
'''