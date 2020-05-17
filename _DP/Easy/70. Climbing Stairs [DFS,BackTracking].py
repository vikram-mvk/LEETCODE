'''
1 dimentional dp
we initially have base cases dp[0],[1],[2]...
for every subsequent recursive call, we record the no.of possible ways for 'n' steps
by storing in dp[n].. which means , dp[5] would represent the nu.of possible ways to go to 5

here we recursively call the n-1 and n-2 th elements as parameters
This is a backtracking problem
At any given point(n) we can either take 1 step or 2 steps
if n=5
then,
         5
        /  \
       4    3 (got from dp)
      /  \
     3    2
    / \  / \
   2   1 1  0
(these 4 values are obtained from dp)
left subtree executes fully.
right subtree gets value from dp


'''
n=5
dp=[0]*(n+1)
dp[0]=0
dp[1]=1
dp[2]=2

def climb(n):
    if n <= 2:
        return dp[n]
    if dp[n] > 0:
        return dp[n]
    dp[n] = climb(n - 1) + climb(n - 2)
    return dp[n]


print(climb(n))