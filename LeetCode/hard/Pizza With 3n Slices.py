class Solution:
    def maxSizeSlices(self, slices):

        # ex) slices = [1,2,3,4,5,6] / k=6
        # 3으로 나눈 만큼 반복하기 때문에 3으로 나눔
        k=len(slices)//3

        # 주어진 배열을 [:-1] 제일 뒤에 값을 제거 / 주어진 배열을 [1:] 첫번째 값을 제거 해서 dp에 돌린다.
        return max(self.dp(slices[:-1], k), self.dp(slices[1:], k))

    #동적 계획법 적용
    def dp(self, slices, k):

        # ex) array = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        array = [[0]*(k+1) for i in range(len(slices)+1)]
        #print(array)
        for i in range(1, len(slices)+1):
            #print('i는:',i)
            for j in range(1, k+1):
                #print('j는:', j)
                if i==1:
                    array[i][j] = slices[i-1]
                    continue
                array[i][j] = max(array[i-2][j-1] + slices[i-1], array[i-1][j])
                #print(array)
        return array[-1][-1]


a=[1,2,3,4,5,6]
test = Solution()
test.maxSizeSlices(a)
