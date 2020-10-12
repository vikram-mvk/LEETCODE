'''
https://leetcode.com/problems/path-sum/
Algorithm:
1. Have a global variable "ans" and assign True only when sum==curr_sum when you reach a leaf node.
2. until then, call root.left with (root.val+curr_sum) and root.right

'''
class Solution:
    ans=False
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def check(root,curr_sum):
            if not root:  return self.ans
            if root.left==None and root.right==None: #in case of a Leaf Node
                self.ans =  sum==curr_sum+root.val  #return value of this expression is sum
                return self.ans
            check(root.left,curr_sum+root.val) #recursive call
            if not self.ans:  check(root.right,curr_sum+root.val)    	#Check right subtree, only when ans is not True
            return self.ans

        return check(root,0) 	#main recursive call. Trace from here