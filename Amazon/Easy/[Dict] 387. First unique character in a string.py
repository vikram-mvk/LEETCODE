'''
https://leetcode.com/problems/first-unique-character-in-a-string/
Store char and index in a dict. if char is present delete it from dict.
if string's index == dict's value, thats the first char

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, x in enumerate(s):
            if x not in d:
                d[x] = i
            else:
                del d[x]
        i = 0

        while i < len(d):
            if i == d[s[i]]:
                return i
            i += 1
        return -1