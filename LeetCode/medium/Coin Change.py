class Solution():
    def coinChange(self,coins:List[int],amount:int) -> int:
        """
           :type coins: List[int]
           :type amount: int
           :rtype: int
       """
        # 임의의 가장 큰값을 만든다
        dp=[float('Inf')]*(amount+1)
        # 0번째 값은 0으로 초기화
        dp[0]=0
        # coins를 오름차순 정렬
        coins.sort()

        for i in range(1,amount+1):
            #print('i는:',i)
            # 임의의 큰 값으로 temp 설정
            temp=[float('Inf')]
            #print(temp)
            for c in coins:
                #print('c는:',c)
                # i가c보다 작다면
                if i-c<0:
                    break
                temp.append(dp[i-c])
            dp[i]=min(temp)+1
            #print(dp)
        return dp[amount] if dp[amount] != float('Inf') else -1