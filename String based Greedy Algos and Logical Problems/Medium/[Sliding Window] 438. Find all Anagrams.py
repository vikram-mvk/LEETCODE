'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Looking at the question we know that we have to store the computed data and not freshly compute the has for the next iteration
Store the frequency of the pattern
Store frequency of the input until 1 - length of the PATTERN. This is done because, we will set a loop into motion, which will add an element to the ip and check if its same as the pattern
if we dont do it until 1-len of patt, then the loop can't check if the first term itself is an anagram. i.,e anagram starting from index 0 will be skipped


start from the len(pattern)-1 th index (last index) and iterate until len of input
now we compute the hash at this location and compare it with the pattern array

if yes we append the index i-len(p)+1..
at i-len(p)+1 do -1
else
we reduce the first element by -1 form ip, append the new element and check again
note, if you delete the first element, its wrong, because its frequency. not a single value

'''

s= "cbaebabacd"
p= "abc"
res = []
ip = [0] * 26
pat = [0] * 26

if len(p) > len(s):
    print([])

for x in p:
    pat[ord(x) - 97] += 1

for x in range(0, len(p) - 1):
    ip[ord(s[x]) - 97] += 1

i = len(p) - 1

while i < len(s):
    ip[ord(s[i]) - 97] += 1
    if ip == pat:
        res.append(i - len(p) + 1)
    ip[ord(s[i - len(p) + 1]) - 97] -= 1
    i += 1
print(res)