'''
https://leetcode.com/problems/same-tree/
We need to stay in root and get back all the results of the recusrive calls
'''
#Iterative
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    stack = [(p, q)]
    while len(stack) > 0:
        p, q = stack.pop(0)
        if not p and not q:  continue
        if not p or not q: return False
        if p.val != q.val: return False
        stack.append((p.left, q.left))
        stack.append((p.right, q.right))

    return len(stack) == 0


#Recursive
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #if both are null return true
    if p == None and q == None:
        return True
    #if only one is null, return False. Not if both are null, prev statement will return True and this will not execute
    if p == None or q == None:
        return False
    #remaining case, both are not null
    if p.val != q.val:
        return False

    l = self.isSameTree(p.left, q.left)
    r=False
    if l:
        r = self.isSameTree(p.right, q.right)

    return l and r
