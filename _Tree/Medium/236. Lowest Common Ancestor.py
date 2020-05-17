'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
    3
   / \
  9  20
    /  \
   15   7
  /
 14

The intuition is given a root node, find all its chilren for P or Q
if one is found, search for the other below you. for ex: if 20 is found, search for other nodes below 20
if found, return 20. else, continue search.
after done searching, return the L or R whichever is not None

'''
#case 1
#p=9
#q=7
#case 2
#p=20
#q=14
def lowestCommonAncestor(self, root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
#whenever a node is found return its parent to left and right variables repectively
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    # if both are found by the same root. they're siblings. so root is the parent
    if left and right:
        return root

    #case 1: 9 will be found in root.left
    #then 20 will be called. its return depends on 15 and 7
    #15 return depends 14, which will return None.
    # 20's L is none and R is 7 (returns itself)
    #now both L and R are true, return root

    elif left:
        return left
    elif right:
        return right
    #This can be roungly translated to, if the node exists return the parent
    return None
'''
When a node is found, we stop searching further down and start backtracking
if other node is also found, we return root
At any point, when two nodes are found we return the root. It is catched by caller's left or right
it doesn't matter because if left is null right will be returned as vice versa
so the original caller will just receive the root node.

'''