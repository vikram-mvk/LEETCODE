'''
If slow and fast are equal at some point, there is a cycle,
When two pointers travel in a loop, they will meet somewhere in the loop.
return true.
Note that this doesn't guarentee that, the meeting point is the beginning of the cycle. its just somewhere in the cycle,
may or may not be the beginning


'''
def hasCycle(self, head: ListNode) -> bool:
    if head == None:
        return False

    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True

    return False
