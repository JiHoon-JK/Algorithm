class Solution(object):
    def rob(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        # rob_helper는 튜플 형태의 값을 반환
        # 첫 번째 값으로는, root를 포함한 경우 / 두 번째 값으로는, root를 포함하지 않은 경우
        # 둘 중에서 큰 값을 리턴해주면 된다.
        best_with_root, best_without_root = self.rob_helper(root)
        return max(best_with_root, best_without_root)

    def rob_helper(self,root):
        # root가 False라면
        if not root:
            return (0,0)

        # root 의 왼쪽 줄기가 루트를 포함한 경우와 포함하지않은 경우
        best_with_root_left, best_without_root_left = self.rob_helper(root.left)
        with_root_left, without_root_left = best_without_root_left, max(best_with_root_left, best_without_root_left)

        best_with_root_right, best_without_root_right = self.rob_helper(root.right)
        with_root_right, without_root_right = best_without_root_right, max(best_with_root_right, best_without_root_right)

        # return 의 첫번째 값은 루트를 포함한 경로 / 두번째 값은 루트를 제외한 경로이다.
        return (root.val + with_root_left + with_root_right, without_root_left + without_root_right)