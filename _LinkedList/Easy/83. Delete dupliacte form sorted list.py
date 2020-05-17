'''
def deleteDuplicates(self, head: ListNode) -> ListNode:
    temp = head
    while head and head.next:
        if head.next.val == head.val:
            head.next = head.next.next
        else:
            head = head.next
    return temp
'''