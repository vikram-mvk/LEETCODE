'''
https://leetcode.com/problems/palindrome-linked-list/
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        slow = fast = head

        if not fast.next:
            return True

        pre = None
        nxt = None
        curr = None

        count = 0
        while fast:
            count += 1
            if fast.next:
                count += 1
                fast = fast.next.next
                curr = ListNode(slow.val)
                curr.next = pre
                pre = curr
                slow = slow.next
            else:
                fast = fast.next

        if count % 2 != 0:
            curr = ListNode(slow.val)
            curr.next = pre

        while slow and curr:
            if slow.val != curr.val:
                return False
            slow = slow.next
            curr = curr.next

        if count % 2 != 0 and curr:
            curr = curr.next

        return slow == curr