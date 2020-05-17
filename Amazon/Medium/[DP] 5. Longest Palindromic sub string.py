'''
The key here is to check the table if the next letter from the start and pre letter from the end is true
table[i+1][last-1]

we create a DP table[][] which maps all the letters with all the other letters in the word.
bcaba is the string

    0 1 2 3 4
    b c a b a
0 b T
1 c  T
2 a    T
3 b      T
4 a        T

Every letter is a palindrome to itself. So we mark T for self. Now we found palindormes of length 1
If adjacent letters are same, then its a palindrome of length 2
then find for length k
loop until k size is last index:
    loop until i is total_size-substr_size:
        if s[i]==s[i+k] and table's one element before these elements. from beginning +1 from end -1
        ie., if s[i]==s[i+k] and table[i+1][i+k-1]:
                update end table=True etc.,
'''
s="bcaba"
len=len(s)-1
table=[[False]*(len+1) for x in range(len+1)]  #2d syntax [ []*(j times) for x in range(i)] adding a list of j elements i times
substr=0
start=end=0
for i in range(0,len+1):
    table[i][i]=True
for i in range(0,len):
    if s[i]==s[i+1]:
        table[i][i+1]=True
        substr=1
        start=end=i

substr=2
i=j=0
while(substr<=len):
    while(i<=len-substr):
        if( s[i] == s[i+substr] and table[i+1][i+substr-1]):
            end=i+substr
            start=i
            table[i][i+substr]=True
        i+=1
    substr+=1
print(s[start:end+1])





