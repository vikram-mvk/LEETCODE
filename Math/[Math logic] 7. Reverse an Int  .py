'''
https://leetcode.com/problems/reverse-integer
when we don't know the length of an int and we need to reverse it,
we just multiply the previous result by 10 everytime so that new number is always added in the units place
'''


def reverse(self, x: int) -> int:
    ans = 0
    flag = False
    if x < 0:
        x = x * -1
        flag = True

    while x > 0:
        ans = (ans * 10) + (x % 10)
        #add a place to insert the number in unit's place
        x = x // 10

    if ans < 2 ** -31 or ans > 2 ** 31 - 1:
        return 0

    if flag:
        return ans * -1
    else:
        return ans
