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