'''
https://leetcode.com/problems/next-greater-node-in-linked-list/
'''

'''
Most Optimal stack approach:
Add new elements in a stack and add 0 for it in res array since we don't yet know if a greater element is gonna come
peek the stack and if current element is greater, assign the current element as the res of all stack elts where curr elt is greater
'''
def nextLargerNodes(self, head: ListNode) -> List[int]:
    res = []
    stack = []
    index = 0
    while head:
        while len(stack) > 0 and stack[-1][1] < head.val:
            res[stack.pop()[0]] = head.val
        stack.append((index, head.val))
        res.append(0)
        index += 1
        head = head.next

    return res


'''
        My Initial Brute force approach:
        For each node, a function will loop through the remaining nodes and
        return 0 if no larger val is found or the val if larger exists
'''
def nextLargerNodes(self, head: ListNode) -> List[int]:
    def find(node,val):
        while node:
            if node.val>val: break
            node=node.next
        return node.val if node else 0

    temp=head
    ans=[]
    while temp!=None:
        ans.append(find(temp.next,temp.val))
        temp=temp.next
    return ans

'''
Stack approach:
> Convert the linkedList to a normal list
> Have stack and res arrays
> Instead of finding a larger element for a given element, we're looping until a larger element is found and 
assigning it to the previously seen smaller elements.. 
> The seen stack will only have elements in descending order because if a larger element is found it is assigned to 
the correspinding smaller element and removed from stack
'''

def nextLargerNodes(self, head: ListNode) -> List[int]:
    ip = []
    while head:
        ip.append(head.val)
        head = head.next

    res = [0] * (len(ip))
    seen = []

    for index, val in enumerate(ip):
        while len(seen) > 0 and seen[-1][1] < val:
            res[seen.pop()[0]] = val
        seen.append((index, val))
    return res
