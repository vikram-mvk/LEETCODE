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
'''