'''
https://leetcode.com/problems/merge-two-binary-trees/

consider t1 as the main tree and add t2 values to t1 and return t1.
Exit condition: return None or return Root

'''
#Soln 1. Create a new treenode using the sum of the two trees
def merge(self, t1, t2):
    if t1 == None and t2 == None:
        return None
    sum = 0
    nodes = [None] * 4
    if t1:
        sum += t1.val
        nodes[0] = t1.left
        nodes[1] = t1.right
    if t2:
        sum += t2.val
        nodes[2] = t2.left
        nodes[3] = t2.right

    root = TreeNode(sum)
    root.left = self.merge(nodes[0], nodes[2])
    root.right = self.merge(nodes[1], nodes[3])
    return root

#add t2's values with t1
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val +=t2.val
        t1.left=self.mergeTrees(t1.left,t2.left)
        t1.right=self.mergeTrees(t1.right,t2.right)
        return t1