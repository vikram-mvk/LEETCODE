s="abc"
if len(s)<2:
        pass
        #return s
i=1
substr=set()
#i goes from 1 to len(s)
while i<len(s)+1:
    for j in range(len(s)):
        print(j,i,len(s[j:]))
        #len of s from j to end is checked with i
        #each time we're looking for a substring of len i
        if len(s[j:])<i:
            print("true")
            break
        print(s[j:j+i])
        substr.add(s[j:j+i])
        print(substr)
    i+=1
substr = sorted(substr)
print(substr[-1])
