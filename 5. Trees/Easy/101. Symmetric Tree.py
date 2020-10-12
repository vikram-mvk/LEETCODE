'''
	1
   / \
  2   2
 / \ / \
3  4 4  3

The key here is to move one node towards the left and other node towards the right and compare their values
At any given point if one node moves left, the other should move right. and vice versa
in left subtree, move left from 2 to find 3 but move right from right subtree to find 3
(look at the figure)

This gives the idea that we need to make a recursive call with recur(root.left, root.right)
'''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recur(root.left, root.right)

    def recur(self, left, right):
        # if both are null, return True
        if not left and not right:
            return True
        # if only one is null return False. (if both are null previous statement will execute)
        if left == None or right == None:
            return False
        # remaining condition is both are not null. so we check their values
        if left.val != right.val:
            return False
        # move left to left and right to right
        l = self.recur(left.left, right.right)
        # only when left subtree is true, we need to check the right.
        r=False
        if l:
            # move left to right and right to left
            r = self.recur(left.right, right.left)

        return l and r