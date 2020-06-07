'''
https://leetcode.com/problems/longest-common-prefix/submissions/
This should be solved using trie

'''
def longestCommonPrefix(strs) -> str:
    prefix = 0
    #index of prefix initially
    if len(strs) < 1:
        return ""
    if len(strs) == 1:
        return strs[0]

    #consider 1st element as the prefix
    compare = strs[0]

    i = 0
    #i can't be bigger than the prefix that we've considered
    while i<len(compare):
        x = 1
        #start from the second word in the array and compare
        for word in range(1, len(strs)):
            if check(strs[word], compare, i):
                x += 1
            else:
                #at any point if the method returns false, there is no point in cheking further
                return compare[0:prefix]

        prefix += 1
        i += 1
    #Worst case: All strings are the same
    return compare[0:prefix]

def check(s, compare, i):
    try:
        if s[i] == compare[i]:
            return True
        else:
            return False
    except:
        return False
print(longestCommonPrefix(["flower","flower","flower"]))
'''
Trie method:

class Trie:
    def __init__(self, val):
        self.children = {}
        self.cnt = 0
        self.character = val

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Trie('#')
        for s in strs:
            cur = root
            for c in s:
                if c not in cur.children:
                    cur.children[c] = Trie(c)
                cur = cur.children[c]
                cur.cnt += 1
        res = ''
        cur = root
        pre = None
        while pre != cur:
            pre = cur
            for child in cur.children.values():
                if child.cnt == len(strs):
                    res += child.character
                    cur = child
        return res
'''