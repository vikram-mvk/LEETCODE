'''
https://leetcode.com/problems/first-unique-character-in-a-string/
Store char and index in a dict. if char is present delete it from dict.
if string's index == dict's value, thats the first char
'''

def firstUniqChar(s: str) -> int:
    d = {}
    for i, x in enumerate(s):  d[x] = i if x not in d else len(s)

    mini = len(s)
    for key, value in d.items():
        if value < mini:  mini = value
    return -1 if mini == len(s) else mini
print(firstUniqChar("leetcodelove"))