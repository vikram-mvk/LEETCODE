'''
Iterative: Do normal level order traversal and reverse the subarray if we're at a odd level.

(Removing the if else statement after if size==0 will result in normal level order traversal)

Recursive: Do the normal recursive level order traversal and append at the last index when we're in a even level. If in an odd level, insert at position 0

'''

class soln:
    def zigzagLevel(self, root):
        if not root: return []
        levels=[]
        def traverse(node,level):
            if not node: return
            if len(levels)<level+1: levels.append([]) #initailly levels is a 1d array. We need to create new [] to append items
            if level%2!=0: levels[level].insert(0,node.val)
            else:levels[level].append(node.val)
            traverse(node.left,level+1)
            traverse(node.right,level+1)
        traverse(root,0)
        return levels


class soln:
    def zigzagLevelOrder(self, root):
        if not root: return []
        levels=[]
        bfs=[root]
        size=len(bfs)
        curr_level=[]
        level=0
        while size>0:
            temp=bfs.pop(0)
            curr_level.append(temp.val)
            if temp.left: bfs.append(temp.left)
            if temp.right: bfs.append(temp.right)
            size-=1
            if size==0:
                level+=1
                size=len(bfs)
            if level%2!=0: levels.append(curr_level[::-1])
            else: levels.append(curr_level)
            curr_level=[]
        return levels
