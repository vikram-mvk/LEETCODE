'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Concept:
For loop inside recursion is often used when we need to go to the last point
and then backtrack from that point

'''
input="23"
d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
res=[]
def dfs(index,combo):
    if len(input)==len(combo):
        res.append(combo)
        return
    else:
        for letter in d[input[index]]:
            dfs(index+1,combo+letter)

dfs(0,"")


print(res)


