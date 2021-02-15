# 최솟값 구하기

arr=[5,3,7,9,2,5,2,6]
# 파이썬에서 가장 큰 값을 저장 (초기화)
arrMin=float('inf')
#0~7까지 총 8번 반복
for i in range(len(arr)):
    if arr[i] < arrMin:
        # for문을 돌면 arr 배열에 가장 작은값이 arrMin에 들어가있다.
        arrMin=arr[i]
'''
# 위와 같은 방법으로도 for문 작성가능
for x in arr:
    if x<arrMin:
        arrMin=x      
'''
print(arrMin)
