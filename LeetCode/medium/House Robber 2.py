class Solution(object):
    def rob(self,nums):
        '''
        :type nums: List[int]
        :return: int
        '''
        # nums=[1,2,3,4,5]
        def houseRobber(nums):
            # 동적계획법을 사용해보자
            dp=[0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2, len(nums)):
                dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            # 가장 큰 값을 dp[-1]을 받음
            return dp[-1]

        # edge cases:
        if len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums)

        return max(houseRobber(nums[:-1]),houseRobber(nums[1:]))

