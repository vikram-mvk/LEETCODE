#lexicographically largest substring

str="baca"
res=[]
for i in range(len(str)):
    for j in range(i,len(str)):
        res.append(str[i:j+1])
res.sort()
print(res)


#one of the best O(N) solution
# https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/361121/Python-O(n)-with-explanation

def maxSubstring(s):
    # Write your code here
    n = len(s)
    starts = list(range(n))
    offset = 0
    while len(starts) > 1:
        letters = []
        for start in starts:
            if start + offset < n:  letters.append(s[start + offset])
        max_end = max(letters)
        new_starts = []
        for i, start in enumerate(starts):
            if i > 1 and starts[i - 1] + offset == start: continue
            if start + offset == n: break
            if s[start + offset] == max_end: new_starts.append(start)
        offset += 1
        starts = new_starts

    return s[starts[0]:]