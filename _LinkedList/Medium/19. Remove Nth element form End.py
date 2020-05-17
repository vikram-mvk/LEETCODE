'''
We need to do it in one pass
so we have fast and slow pointers.
Move fast pointer until N first.
its like subtracting from the end
'''

'''
if n < 1:
    return head
fast = head
slow = ListNode(0)
slow.next = head
ans = slow
for x in range(n - 1):
    fast = fast.next
while fast and fast.next:
    fast = fast.next
    slow = slow.next
slow.next = slow.next.next
return ans.next
'''