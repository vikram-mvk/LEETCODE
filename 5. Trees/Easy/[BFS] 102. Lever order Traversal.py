'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
#All elements in the same level should be in the same sub array
    3
   / \
  9  20
    /  \
   15   7

output:
[ [3],  [9,20],  [15,7] ]

    1
   / \
  2   3
 /     \
4       5

output:
[[1],[2,3],[4,5]]
'''
#Recurise solution
'''
When it is at the same level, it appends at the same array index
'''
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    levels = []
    
    def traverse(node, level):
        if not node: return
        if len(levels) < level + 1: levels.append([]) #create a new space for inserting
        levels[level].append(node.val)
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)

    traverse(root, 0)
    return levels


#Iterative soln 1 single while loop reassing
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    levels = []
    bfs = [root]

    #initial size. children will be added for initial size.
    size = len(bfs)
    curr_level = []
    while size > 0:
        temp = bfs.pop(0)
        curr_level.append(temp.val)
        if temp.left: bfs.append(temp.left)
        if temp.right: bfs.append(temp.right)
        size -= 1
        if size == 0: #when initial size is zero, reassign size, to add their children
            size = len(bfs)
            levels.append(curr_level)
            curr_level = []
    return levels

#two while loops
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        bfs = []
        bfs.append(root)
        size=len(bfs)
        while len(bfs) > 0:
            children = []

            #until initial queue is empty. will prevent adding new nodes in the same subarray
            while size > 0:
                node = bfs.pop(0)
                children.append(node.val)
                #add the node's value
                size -= 1
                #append current node's children to queue. This will not affect size variable
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)

            #append the subarray
            ans.append(children)
            #reset queue size
            size=len(bfs)
        return ans