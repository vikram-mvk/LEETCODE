#https://leetcode.com/problems/top-k-frequent-words/

'''
My Code:
1. Find frequency of each word using d
2. create a freq array where indices represent freq. Append words to d's value (i.e., word's frequency)
3. sort the freq sub array, if it has more than one element

Mokka code:
1. Sort by alpha
2. Sort the resulting tuple by freq (tuple's second parameter)
'''

# we're saving a lot of time by avoiding sorting by frequency and also by sorting by alphabets only when more than one words have the same frequency
words=["i", "love", "leetcode", "i", "love", "coding"]
k = 2

d = {}
frequency = [[] for i in range(len(words))]
for x in words: d[x] = 0 if x not in d else d[x] + 1  # find frequency of each word

for key, val in d.items(): frequency[val].append(key)  # append the words in frequency array according to word frequency

i = len(frequency) - 1  # a pointer to append last k values (k most frequent) to a new array
res = []

while len(res) < k and i >= 0:

    if len(frequency[i]) > 1: frequency[i].sort()  # if more than 1 elements have same frequency, sort it by alphabetical order

    for x in frequency[i]:
        if len(res) == k: break
        res.append(x)  # append the sorted sub array elts in res

    i -= 1

print(res)

'''
# 8 line version
d, frequency = {}, [[] for i in range(len(words))]
for x in words: d[x] = 0 if x not in d else d[x] + 1
for key, val in d.items(): frequency[val].append(key)
i, res = len(frequency) - 1, []
while len(res) < k and i >= 0:
    if len(frequency[i]) > 1: frequency[i].sort()
    for x in frequency[i]:
        if len(res) < k: res.append(x)
    i -= 1

return res
'''

'''

Mokka code from discussion where they sort twice.

def topKFrequent(self, words: List[str], k: int) -> List[str]:
    # frequency=[ [] for i in range(len(words)) ]#Frequency of any word can't be greater than the length of the array
    d = {}
    for x in words:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    # sort by alphabetical order
    alpha = sorted(d.items(), key=lambda x: x[0])
    # sort the resulting frequency
    freq = sorted(alpha, key=lambda x: x[1], reverse=True)
    # we now have a tuple, which is first sorted by alpha then by freq. get the 0th index alone from the tuple
    res = []
    i = 0
    while i < k:
        res.append(freq[i][0])
        i += 1
    return res
'''