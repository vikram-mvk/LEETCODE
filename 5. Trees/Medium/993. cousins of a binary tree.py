'''
https://leetcode.com/problems/cousins-in-binary-tree/

1. we return 0 if x or y is null and we return 1 if x or y is present. (Similar to max depth of binary tree)
Return value is multiplied by 2 on every return. using this we can find the depth of the x and y nodes.
2. Save the parent in global variable before going left or right
2. compare the parents and depths and return accordingly.
'''
class Solution:
    parent = None
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
         #silly test cases
        if root==None or root.left==None or root.right==None: return False
        if root.val==x or root.val==y: return False
        if root.left.val+root.right.val == x+y: return False

        def find(node,search):
            if node==None: return 0
            if node.val==search: return 1
            self.parent=node
            depth=find(node.left,search)*2
            if depth==0:
                self.parent=node
                depth=find(node.right,search)*2
            return depth

        self.parent=root
        xdepth=find(root.left,x)
        if xdepth==0: xdepth=find(root.right,x)
        xparent=self.parent

        self.parent=root

        ydepth=find(root.left,y)
        if ydepth==0: ydepth=find(root.right,y)
        yparent=self.parent

        return xdepth==ydepth and xparent!=yparent








'''
    # Code with explanation


class Solution:
    parent = None

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        # First we deal with the annoying silly test cases like the below 4
        if root == None:
            return False
        # if either x or y, then x and y depth will not be same. so False

    if root.val == x or root.val == y:
        return False
        # both left and right must be present
    if root.left == None or root.right == None:
        return False
        # if x and y are immideate children of root, return False
    if root.left.val + root.right.val == x + y:
        return False


    About the depth function
    We return 0 if x or y is not found,
    We return 1 if x or y is found.
    return value will be multiplied by 2, each time it backtracks
    0*anything is always 0. so it helps us know that its not found yet
    when its 1, it gets multiplied by 2 everytime. so the actual depth will be final return value/2. 
    but we dont care about the actual depth. we just need to make sure that the depths are same.


    def depth(node, search):
        if node == None:
            return 0
        if node.val == search:
            return 1
        self.parent = node
        found = depth(node.left, search) * 2
        # if found in the left subtree, dont search right subtree. search only when not found. i.,e return value is 0
        if found == 0:
            self.parent = node
            found = depth(node.right, search) * 2

        return found

    # initally parent is root. It gets updated in dfs call
    self.parent = root

    onedepth = depth(root, x)
    oneparent = self.parent

    # reassign it to root
    self.parent = root

    otherdepth = depth(root, y)
    otherparent = self.parent

    return onedepth == otherdepth and oneparent != otherparent

soln 1
def dfs(node, parent = None, lvl = 0):
        if node:
            node.parent = parent

            if node.val == x:
                self.x_node = node
                self.x_lvl = lvl
            elif node.val == y:
                self.y_node = node
                self.y_lvl = lvl

            dfs(node.left, node, lvl + 1)
            dfs(node.right, node, lvl + 1)

    dfs(root)

    if self.x_lvl == self.y_lvl and self.x_node.parent != self.y_node.parent:
        return True
    else:
        return False
'''