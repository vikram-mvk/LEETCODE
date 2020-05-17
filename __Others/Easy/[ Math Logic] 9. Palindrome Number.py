'''
https://leetcode.com/problems/palindrome-number/
'''
def isPalindrome(self, x: int) -> bool:
    # negative numbers are not gonna be palindromes
    if x < 0:
       return False

    ans = 0
    ip = x
    # Get the last digit and add it to ans's unit's place. do ans*10 to create a new unit's place.
    # for ex: if you want to add 2 to 11. you need to 11*10 => 110 +2 => 112
    while x > 0:
        ans = (ans * 10) + x % 10
        x = x // 10
    return ip == ans
