'''
https://leetcode.com/problems/palindrome-linked-list/
'''

def isPalindrome(self, head: ListNode) -> bool:
    if not head: return True

    # find the size of the linkedlist
    size, temp = 1, head
    while temp and temp.next: temp, size = temp.next, size + 1

    if size == 1: return True
    if size == 2: return head.val == head.next.val

    # reverse the first half
    slow = fast = head
    pre = None
    while fast and fast.next:
        fast = fast.next.next
        nxt = slow.next
        slow.next = pre
        pre = slow
        slow = nxt

    # if its an odd size, the middle element doesn't matter. to move nxt one point
    if size % 2 != 0: nxt = nxt.next

    while nxt and pre:
        if pre.val != nxt.val: return False
        pre = pre.next
        nxt = nxt.next

    return True