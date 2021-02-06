class Solution:
    def isSubPath(self, head, root):
        # root = false , head = false
        if not root and not head:
            return True
        elif not root or not head:
            return False

        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == head.val and self._is_sam(curr, head):
                return  True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return False

    def _is_same(self,root,head):
        stack = [(root, head)]

        while stack:
            curr_tree, curr_list = stack.pop()
            if not curr_list.next:
                return True
            if curr_tree.left and curr_tree.left.val == curr_list.next.val:
                stack.append((curr_tree.left, curr_list.next))
