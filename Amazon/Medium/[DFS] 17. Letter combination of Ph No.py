'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Problem:
iterative is difficult because we need to dynamically create for loop
queue can be used to solve it.
in recursion call stack is being used like a queue

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


