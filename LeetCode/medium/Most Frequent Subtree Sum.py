# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):

        # subtree_sum 의 {값 : 빈도} 를 보여줄 딕셔너리를 만든다.
        self.subtree_sum_dict = {};

        # 서브트리의 합 중에서 제일 많이 나타난 주기에 대한 초기값 (처음은 0으로 잡는다.)
        self.highest_frequency = 0

        # 서브트리에서 제일 많이 나타난 값을 기록한다.
        # 배열의 값으로 return 해야하기 때문에 초기값은 []
        self.highest_freq_sum = []

        # =======================================================
        def helper(node):
            # 노드가 없다면
            if not node:
                #노드가 없으면 아무것도 없는 트리이다.
                return 0
            # 노드가 있다면
            else:
                # 노드의 왼쪽 줄기의 합
                left_sum = helper(node.left)
                # 노드의 오른쪽 줄기의 합
                right_sum = helper(node.right)

                # 노드의 총합
                cur_sum = left_sum + node.val + right_sum

                # get(키, 기본값)
                # self.subtree_sum_dict 딕셔너리에서 cur_sum 이라는 키를 정의한다.
                # self.subtree_sum_dict.get(cur_sum,0) : cur_sum 키가 없으면 0을 반환 , cur_sum 의 value 값을 등록
                self.subtree_sum_dict[cur_sum] = self.subtree_sum_dict.get(cur_sum,0) + 1

                # 가장 빈번한 주기보다 다 더한 값의 주기가 더 많거나 같다면
                if self.subtree_sum_dict[cur_sum] >= self.highest_frequency:
                    if self.subtree_sum_dict[cur_sum] > self.highest_frequency:
                        # 가장 빈번한 주기보다 다 더한 값의 주기가 많다면
                        # self.highest_frequency 를 cur_sum의 주기로 바꾼다.
                        self.highest_frequency = self.subtree_sum_dict[cur_sum]
                        self.highest_freq_sum = []

                    # 가장 빈번한 주기와 다 더한 값의 주기가 같다면,
                    # 가장 빈번한 주기일 때 합을 업데이트한다. {cur_sum : cur_sum_frequecnt}
                    self.highest_freq_sum.append(cur_sum)

                # 가장 빈번한 주기보다 다 더한 값의 주기가 더 적다면
                return cur_sum
        # ======================================================

        helper(root)
        # 해당 코드의 결과값은 제일 빈번한 주기의 합을 [] 형태로 반환해야한다.

        print(self.subtree_sum_dict)
        print(self.highest_frequency)
        print(self.highest_freq_sum)

        return self.highest_freq_sum