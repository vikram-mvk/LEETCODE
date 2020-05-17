'''
Recall 1 dimentional dp in climbing stairs
we initially have base cases dp[0],[1],[2]...
for every subsequent recursive call, we record the no.of possible ways for 'n' steps
by storing in dp[n].. which means , dp[5] would represent the nu.of possible ways to go to 5

similarly, here we need to store the values for every iteration, i.e., if len of text1 is 3 and text2 is 2 .. we need to store 6 values
which represent the max subsequence in that iteration

two dimensional dp
Its basically looking up values from all the previous iterations
we check the immideate top row of the same column or the immediate left column of the same row because it has stored the value with which we can safely skip this character. It represents the sub sequence that we were previously dealing with

Initially fill all the rows and cols of dp with 0
we start the loop from 1
we check if the elements at the 0th index of text1 and 2 are the same.
if yes, we update the dp[1][1] as 1
which indicates, at the iteration i=1,j=1 we found 1 subsequence
since we're looping text2's each character with all the chars of text1
the subsquence of text2 in text1 is recorded in dp

if two chars are not equal,
we update the dp[i][j] to max of
previous column of the same row
(this basically getting the sub seq length when we were dealing with text2's ith char and text1's j-1th char
for ex: text2's a== text1's a when i=1 and j=1
)

or
previous row of the same column
(this basically getting the sub seq length when we were dealing with text2's i-1 th char and text1's jth char
for ex: text2's a== text1's 0th index (which is 0) when i=1 and j=1
)
'''
text1="abcde"
text2="ace"
rows = len(text2)
cols = len(text1)
dp = [[0] * (cols + 1) for x in range(rows + 1)]

for i in range(1,rows + 1):
    for j in range(1,cols + 1):
        if (text2[i - 1] == text1[j - 1]):
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[rows][cols])

'''
Recursive approach with LRU cache(DP)
@lru_cache(maxsize=None) # This memoize the function calls with arguments and returned results so that you can call again later on with same parameters without incurring additional computation. Max_size specifies that our LRU cache can grow without bounds.
        def memo_solve(ptr1, ptr2):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            
            # Case 1
            if text1[ptr1] == text2[ptr2]:
                return 1 + memo_solve(ptr1+1, ptr2+1)
        
            # Case 2
            else:
                return max(memo_solve(ptr1+1, ptr2), memo_solve(ptr1,ptr2+1))
                            # ^ Case 2 - Option 1           ^ Case 2 - Option 2
        return memo_solve(0,0) # Start the recursion stack from str1[0] and str2[0]				

'''