import sys
sys.stdin=open("input.txt","rt")

def check(a):
    for i in range(9):
        check_rows = [0] * 10
        check_cols = [0] * 10
        for j in range(9):
            check_rows[a[j][i]]=1
            check_cols[a[i][j]]=1
        # 행이나 열에 1~9까지에서 하나씩 가지지 않는 경우
        if sum(check_rows) != 9 or sum(check_cols) != 9:
            return False

    for i in range(3):
        for j in range(3):
            check_boxs = [0] * 10
            for k in range(3):
                for s in range(3):
                    check_boxs[a[i*3+k][j*3+s]]=1
            if sum(check_boxs) != 9:
                return False
    return True

a=[list(map(int,input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")