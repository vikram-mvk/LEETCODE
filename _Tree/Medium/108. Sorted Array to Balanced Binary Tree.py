'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

To make the binary tree balanced, we need to choose the mid element of the array at each function call

input: [-10,-3,0,5,9]
Expected output :
      0
     / \
   -3   9
   /   /
 -10  5
Print output(backtrack from leaf):
TreeNode{val: -10, left: None, right: None}
TreeNode{val: -3, left: TreeNode{val: -10, left: None, right: None}, right: None}
TreeNode{val: 5, left: None, right: None}
TreeNode{val: 9, left: TreeNode{val: 5, left: None, right: None}, right: None}
TreeNode{val: 0, left: TreeNode{val: -3, left: TreeNode{val: -10, left: None, right: None}, right: None}, right: TreeNode{val: 9, left: TreeNode{val: 5, left: None, right: None}, right: None}}
'''


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        return self.recur(nums, 0, len(nums) - 1)

    def recur(self, nums, l, r):
        if l > r:
            return None
        mid = (l + r + 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.recur(nums, l, mid - 1)
        root.right = self.recur(nums, mid + 1, r)
        print(root)  # will print when backtracking all the way to root. you can see nodes attaching to their parent's left and right

        return root