'''
Approaches:

Two pointer approach (One pass, to point to a previous variable in a loop)
---------------------------------------------------------------------------
Recursion vs Iterative

---------------------------------------------------------------------------
DP
Reduce the repetition by storing computed values
ex: climbing stairs, product of array exept self
---------------------------------------------------------------------------
TREES:

DFS is by recursion
BFS is by queue

1. Always stay in the root and get back values from other calls, unless otherwise required
2. If we want to check something for every node, then use L and R variables and
stay in root if we need to do specific action based on the L and R variables
otherwise we can directly make the recursive call from the return statement
----------------------------------------------------------------------------
LINKEDLIST:
Always remember to make changes only using a next pointer
curr.next=something will change the reference of curr's next
whereas
curr=curr.next and then doing curr=something,
will not affect the next pointer. you're just reassigning the curr ptr

Slow Fast Pointer

1. For middle of a LL, the fast pointer runs twice as fast as slow and hence when you return slow ptr, it returns the middle of the LL
2. For deleting the middle of a LL , use the same slow pointer with slow=LinkedList(0) and slow.next to head, so that we can go one node less than  that of middle due to the addition of 0
3. For loop in a linkedList where we check if slow==fast and at some point it would be true if it has a loop

-----------------------------------------------------------------------------
'''