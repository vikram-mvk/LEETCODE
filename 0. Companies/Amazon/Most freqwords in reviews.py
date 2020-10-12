#https://leetcode.com/discuss/interview-question/542597/

k=2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
freqArr = [ [] for x in range(len(keywords))] #create a 2d array where index represents freq and items at index represent words occouring at that frequency
keyword_set=set() #to remove duplicate and to quickly check if a word in review is a keyword
for i in range(len(keywords)): keyword_set.add(keywords[i].lower())
score={}
for review in reviews:
    for word in set(review.split(" ")):
        #make it lower case, remove periods and spaces
        small=word.lower()
        small=small.replace(".","")
        small=small.strip()

        if small in keyword_set:  score[small]=0 if small not in score else score[small]+1


for key,val in score.items():freqArr[val].append(key)

ans=[]
i=len(freqArr)-1
print(freqArr)
while k>0 and i>0:
    freqArr[i].sort()  #when there are more than 1 word at a given freq, we need to get the items in lexico order, so sort
    for x in freqArr[i]:
        if k<=0: break
        ans.append(x)
        k-=1
    i-=1

print(ans)



