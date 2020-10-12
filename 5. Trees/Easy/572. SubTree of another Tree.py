class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s and t:
            if s.val == t.val and self.isSameTree(s, t): return True
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if s == None and t == None: return True
        if s == None: return False
        if t == None: return False
        if s.val != t.val: return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
