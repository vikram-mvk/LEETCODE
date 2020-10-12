#recursive
'''
Everytime when going left, update only the maxi, which means that curr val must be lesser than maxi and greater than
-inf
everytime when you go right, the root's root's root.val will be maxi(value of root two nodes before now),
and mini will be value of root.
so right must not be lesser than mini and no greater than maxi which is two nodes before the root
'''
class Solution:

    def isValidBST(self, root: TreeNode) -> bool:

        def isValid(root, maxi, mini):
            if not root: return True
            if root.val >= maxi or root.val <= mini: return False
            return isValid(root.left, root.val, mini) and isValid(root.right, maxi, root.val)

        return isValid(root, float('inf'), -float('inf'))
class soln:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        left_child_val = float('-inf')
        # compares left child of a node with the node's left most parent
        # vice versa for right
        while root != None or len(stack) > 0:
            while root != None:  # append all the left nodes in the stack
                stack.append(root)
                root = root.left

            # after its done,  pop the last inserted element(leaf)
            root = stack.pop()
            if root.val <= left_child_val: return False  # if leaf is lesser than -inf, return 0. update comaprision value to current node's value
            left_child_val = root.val
            root = root.right  # assigning will append right node's left nodes to the stack because of nested while loop

        return True

