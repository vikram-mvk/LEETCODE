'''
https://leetcode.com/problems/longest-substring-without-repeating-characters
'''
s="bwwkew"
i = j = ans = 0
d = {}

while i < len(s):
    if s[i] not in d:
        d[s[i]] = 1
        i += 1
    else:
        ans = max(ans, len(d))
        del d[s[j]]  # we dont need ordered dict because we refer to key using the string index from 0.. so other words that we need wont be deleted
        j += 1
ans = max(ans, len(d))  # this is the case for single letter.. else condition will never occur here
print(ans)





