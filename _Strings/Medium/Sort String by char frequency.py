'''
https://leetcode.com/problems/sort-characters-by-frequency/
Main concern: Case sensitive sorting
Find the frequenet=cy using d
sort the d by values
append to an array and join it as a string
'''
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
