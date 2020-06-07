#https://leetcode.com/problems/reorder-data-in-log-files/
'''
1. Check if 1st word after id is a digit or alpha
2. if alpha add in alpha array , if digit, digit array
3. sort alpha array by 0th index (sort by id first)
4. then sort the array by remaining elements ( array[1:] )

by doing this, the words haiving the same content it will be ordered by array index
example:
k2 car was behind g1 car since ordered by id.
when sorting by word since both are car, k2 car will come first,
there will be a clash and it will take the original position.. g1 car first

['a8 act zoo', 'ab1 off key dog', 'g1 act car', 'k2 act car', 'a1 9 2 3 1', 'zo4 4 7']
['g1 act car', 'k2 act car', 'a8 act zoo', 'ab1 off key dog', 'a1 9 2 3 1', 'zo4 4 7']

'''
#logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act car"]
logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","k2 act car"]
digit = []
letter = []
for log in logs:
    if log.split()[1].isdigit(): #if word after id is a digit, same ordering
        digit.append(log)
    else:
        letter.append(log)
letter.sort(key=lambda x: x.split()[0]) #for each log, split the log and sort it by its id
letter.sort(key=lambda x: x.split()[1:]) #for each log, split and sort it by the rest of the word
print(letter + digit)
#Method 2
#My ususal way of using an array where indices represent alphabets or frequeny
digit = []
letter = [ [] for i in range(26)]
for log in logs:
    first_letter=log.split()[1][0]
    if first_letter.isdigit(): #if the first letter after id is a digit, same ordering as original
        digit.append(log)
    else:
        letter[ord(first_letter)-97].append(log)
#now letter holds 'a' logs in 0th index 'b' log in 1st 'c' in 2nd etc..,
res=[]
for x in letter:
    if len(x)>1:
        x.sort()  #sub array sorted by identifier
        x.sort(key=lambda x:x.split()[1:]) #sort by words after id. if the words same, leave it at the previous identifier order
    for items in x:
        res.append(items)
for x in digit:
    res.append(x)
print(res)


'''


def alpha(word): #this will return the ascii value of the first letter after id
            i = 0
            for x in word:
                if x == ' ': break
                i += 1
            return ord(word[i+1])

        ans = [[] for i in range(27)] #a 2d array where indices represent alphabets' asci.. a=0 b=1 c=2 etc....
        digits=[]
        i=0
        
        for x in logs:
            asci = alpha(x)
            if asci > 96 and asci < 123: #if its a letter, append in the respective index
                ans[asci-97].append(x)
            else:
                digits.append(i) #if its a digit, record its original order using index
            i += 1
        res=[]
        
        for x in ans:
            if len(x)==1: 
                res.append(x[0])
            if len(x)>1:
                x.sort(key=lambda w: w.split()[0]) #for each log, split the log and sort it by its id
                x.sort(key=lambda w: w.split()[1:]) #for each log, split and sort it by the rest of the word
                for w in x:
                    res.append(w)
              

        for i in digits:
            res.append(logs[i])
        return res

'''


