'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
You have to be in the root element to count the branches in left and right
by calling both the methods in a return statement, we can know if its a leaf node or not
when moving from an edge towards the top, we add +1 everytime

    3
   / \
  9  20
    /  \
   15   7

'''

#solution 1
def recur(self, node):
    if node == None:
        return 0

    left = self.recur(node.left) + 1
    right = self.recur(node.right) + 1
    #all the recursive call's return are sent back until the original call
    #left and right variable values updated in original call
    if left > right:
        return left
    else:
        return right

#soln 2
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
