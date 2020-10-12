'''
https://leetcode.com/problems/remove-linked-list-elements/
'''
def removeElements(self, head: ListNode, val: int) -> ListNode:
    # for moving through the list
    curr = ListNode()
    curr.next = head

    # for returning
    original = ListNode()
    # initially we assume that all node's val == val. so next will be None
    original.next = None

    copy = original
    # for modifying the original's next pointer

    while curr:
        # if next node exitst and its value is same as val, we skip the next node and go to next.next
        if curr.next and curr.next.val == val:
            curr.next = curr.next.next
        else:
            # if is not equal to val we insert it as original's next (by modifying copy's reference)
            copy.next = curr.next

            # move to curr node's next to find the next node whose value is not equal to val
            copy = copy.next

            curr = curr.next

    return original.next
