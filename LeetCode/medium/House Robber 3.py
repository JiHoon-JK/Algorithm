class Solution(object):
    def rob(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        def dfs(node):
            #None이라면
            if not node:
                return 0,0
            YES_left, NO_left = dfs(node.left)
            YES_right, NO_right = dfs(node.right)
            return node.val + NO_left + NO_right, max(YES_left, NO_left) + max(YES_right, NO_right)

        return max(dfs(root))