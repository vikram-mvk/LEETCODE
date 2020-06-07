class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def recur(root):
            if not root: return None
            temp=root.left
            root.left=recur(root.right)
            root.right=recur(temp)
            return root
        return recur(root)
