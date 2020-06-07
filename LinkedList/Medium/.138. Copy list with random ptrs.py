'''
https://leetcode.com/problems/copy-list-with-random-pointer/

The Idea is to store the node as key and its clone as value in a dictinary
so that we can create the clones by looping once
and create the random references by looping the next time
'''
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        d = {}
        copy = Node(0)
        ans = copy
        temp = head
        # To make a flow in the for loop, we create a node copy with value 0 in the beginning and
        # We insert new node as copy's next

        while temp != None:
            # create a new node (clone)
            copy.next = Node(temp.val)

            # which can be accessed by original node
            d[temp] = copy.next

            # move pointers
            copy = copy.next
            temp = temp.next

        #mark the end of the list, temp becomes none before copy
        copy.next=None

        # now all our clones have the value and next ptr

        temp = head

        # now we need to set random ptrs
        # note that d[something] will give us the clone node
        while temp != None:
            if temp.random != None:
                # original node's random ptr's dict value will give us the clone we need to point to
                d[temp].random = d[temp.random]
            else:
                d[temp].random = None
            temp = temp.next
        return ans.next