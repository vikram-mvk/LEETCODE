def getDecimalValue(self, head: ListNode) -> int:
    ans = 0
    while head:
        ans = ans * 2 + head.val
        head = head.next
    return ans

'''
Instead of doing num*2^0 2^1 .... from back 
we can just multiply existing ans *2 everytime there is a next value
'''