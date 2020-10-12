'''
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

It is quite obvious that to get the tree with smallest sum of non-leaf nodes, the tree must be built by using the smallest elements in the array. 
Since these elements represent an in-order traversal of the tree, we can only multiply adjacent elements.

So we greedily pick the minimum value from the array and check its left and right neighbour's value. We pick the one that is minimum among them and multiply with our minimum
and add it to the result.
Then we drop the minimum element.

In case if there is no neighbour for the min (if it is in a boundary), we multiply the minimum element with min_i - 1 element and add it to our result.
'''
arr=[6,2,4]
res=0
while len(arr)>1:
        mini=arr.index(min(arr))
        if 0<mini<len(arr)-1:
            closest=min(arr[mini-1],arr[mini+1])
            res+=closest*arr[mini]
        else:
            res+=arr[mini]*arr[0] if mini!=0 else arr[mini]*arr[len(arr)-1]
        del arr[mini]
print(res)

'''
 math
 def calculateCost(arr):
    # Write your code here
    res=0
    while len(arr)>1:
        min_index=findmin(arr)
        if 0<min_index<len(arr)-1:
            closest=min(arr[min_index+1],arr[min_index-1])
            res+=arr[min_index]*closest
        else:
            res+=arr[min_index]*arr[1] if min_index==0 else arr[min_index]*arr[min_index-1]
            
        del arr[min_index]
    return res

def findmin(arr):
    min=arr[0]
    i=0
    for index,item in enumerate(arr):
        if item<min:
            min=item
            i=index
    return i





'''



'''
1130. Minimum Cost Tree From Leaf Values

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.


Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
'''
