# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # root : 현재 노드 / 0 : 인덱스에서의 위치 값
        queue = [(root,0)]
        width_max = 0
        #print(queue)

        while queue:
            tmp = []
            # queue 안에 node와 pos를 반복
            for node, pos in queue:
                #print(node)
                #print(pos)
                # node의 왼쪽 값이 있다면
                if node.left:
                    # tmp에 append()를 통해서 (node.left, pos*2) 를 더한다.
                    tmp.append((node.left, pos*2))
                # node의 오른쪽 값이 있다면
                if node.right:
                    #tmp에 (node.right, pos*2+1)을 더한다.
                    tmp.append((node.right, pos*2 +1))

            #print(queue)
            # 너비를 구한다. (큰 값 - 작은 값)
            width = queue[-1][1] - queue[0][1] + 1
            #  width_max와 width 중에서 제일 큰 값을 width_max에 선언
            width_max = max(width_max, width)
        # width_max 제일 큰 너비 값을 반환한다.
        return width_max