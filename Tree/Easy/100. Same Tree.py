'''
https://leetcode.com/problems/same-tree/
We need to stay in root and get back all the results of the recusrive calls
'''
#soln 1
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




#soln 2
flag=True
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return self.flag
    if p and q:
        if p.val!=q.val:
            self.flag=False
            return self.flag
    if (p and not q) or (q and not p):
        self.flag=False
        return self.flag

    self.isSameTree(p.left,q.left)
    self.isSameTree(p.right,q.right)
    return self.flag

