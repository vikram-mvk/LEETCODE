'''
Steps to solve:
For purely Logical problems:
Think of how would i do it with hand if i was asked to solve
implementation of the logic: think of similar questions, templates or different data structures that can be used for that
Think of the most important deciding factor for the result

1. Observation . This is no.1 because there is always a pattern in every problem, and observe the pattern deeply to frame your logic
2. templates. there is always a problem similar to this problem. first try to figrue out the similar problem and analyse the differences if similar problem exist
3. identify why it cannot be solved easily. narrow down to major test cases that are the core of the question and solve it first


Tips and concepts:
1. Two pointer approach (One pass, to point to a previous variable in a loop)
2. If you wanna sort something by 2 params, like by both alpha and frequency, sort it first by alpha so that when
freq is same, then the original position(sorted by alpha) will remain.
3. In recursion, Use L and R all the time, unless its impossible
4. In linkedList, Slow fast pointer
5. In strings, use an array with indices representing frequency or alphabets i.,e -> ord(x)-97
---------------------------------------------------------------------------
Recursion vs Iterative

---------------------------------------------------------------------------
DP
Identification: What is the sub problem here? At any given point what is the action that I'm supposed to take?

When an optimal sub structure and repeacting sub problems exists, DP is possible
Reduce the repetition by storing computed values ex: climbing stairs, product of array exept self
Steps:
1. Start with the recursive backtracking solution
2. Optimize by using a memoization table (top-down[2] dynamic programming)
3. Remove the need for recursion (bottom-up dynamic programming)
4. Apply final tricks to reduce the time / memory complexity
----------------------------------------------------------------------------

TREES:

DFS is by recursion
BFS is by queue
Use L and R all the time, unless its impossible

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