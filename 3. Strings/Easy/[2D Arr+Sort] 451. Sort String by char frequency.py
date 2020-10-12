'''
https://leetcode.com/problems/sort-characters-by-frequency/

'''


def frequencySort(s: str) -> str:
    d, frequency = {}, [[] for i in range(len(s))]
    for x in s: d[x] = 0 if x not in d else d[x] + 1
    for key, value in d.items(): frequency[value].append(key)
    i, ans = len(s) - 1, []
    while i >= 0:
        if len(frequency[i]) > 1:
            frequency[i].sort()
        for x in frequency[i]:
            ans.append(x * (i + 1))
        i -= 1
    print("".join(ans))

frequencySort("tree")
'''
Main concern: Case sensitive sorting
Find the frequenet=cy using d
sort the d by values
append to an array and join it as a string

class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        d = {}
        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        ans = []
        a = sorted(d.items(), key=lambda x: x[1], reverse=True)

        for x in a:
            ans.append(x[0] * x[1])

        return "".join(ans)
        '''
