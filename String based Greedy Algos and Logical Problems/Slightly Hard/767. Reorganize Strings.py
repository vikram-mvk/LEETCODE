'''
Heap solution basic idea:
We build a frequency dict of the letters in the string. We push all the letters into a max heap together with their -ve frequencies (max heap: high-freq letters are towards the top of the heap)
We pop two letters at a time from the heap, add them to our result string, decrement their frequencies and push them back into heap. Why do we have to pop two items/letters at a time you're wondering? Because if we only pop one at a time, we will keep popping and pushing the same letter over and over again if that letter has a freq greater than 1. Hence by popping two at time, adding them to result, decrementing their freq and finally pushing them back into heap, we guranatee that we are always alternating between letters.

For example: for the string s = aab
The freq dict will be: d = {"a": 2, "b":1}
And the heap: h = [(-2, "a"), (-1, "b")]

After the first iteration:
h = [(-1, "a")]
and so on...
Edge Case:
NOTE [1]

Since we are always popping two items at a time, we will definitely run into an out of bounds error if we have an odd number of unique items in the given string. To avoid this, we need to make sure our heap at least has two items at any given time. We achive this by running our main logic inside a while len(heap) > 1 instead of a while heap
NOTE [2]

Again if the there is an odd number of unique letters in the string, there will be one last item/letter remaining in the heap when our loop terminates. Hence we need to examine that last item:
If the last item has a freq greater than 1: -> then return "" becasue we can't escape having the same letter repeated contigiously.
else if the item has freq = 1, we pop it, add it to our result and we're done.
'''
#Non heap solution
class Solution:
    def reorganizeString(self, S):

        # create a char : freq dict
        char_freq = {}
        for char in S: char_freq[char] = 1 if char not in char_freq else char_freq[char] + 1

        # Sort it by frequency
        char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

        # The result is a list of tuples sorted by most frequent to least frequent

        # take the most freq char and its freq
        char, freq = char_freq[0][0], char_freq[0][1]

        # if the highest freq is greater than half the length of the string we cant avoid placing chars adjacent. So return ""
        if freq > (len(S) + 1) // 2:  return ""

        # create a res array containing the most freq char for its freq times
        res = [char] * freq

        # we are going to attach other characters with this character
        # other characters are going to have frequency less than or equal to this character
        # so we won't get any adjacent character while doing attaching other characters

        # main idea is to attach the chars at the last_seen index. This index will increment each time and when goes out of bound, it will come back to 0
        last_seen = 0
        for c, f in char_freq[1:]:  # leaving the most freq pair
            # append the next freq char in cyclic form at each index until its freq
            for i in range(f):
                res[last_seen] += c
                last_seen = (last_seen + 1) % len(res)
                # use modulo to check out of bounds.

        return "".join(res)
#Heap solution
def reorganizeString(S):
    if not S:
        return ""
    # Build freq dict:
    d = {}
    for c in S:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    # push (-ve frq, char) pairs into heap
    h = []
    from heapq import heappush, heappop
    for k in d:
        heappush(h, (-d[k], k))

    res = ""
    # pop and examine frq and append to res
    while len(h) > 1:  # -------------------------------- NOTE [1]
        f1, c1 = heappop(h)
        f2, c2 = heappop(h)

        res += c1
        res += c2

        if abs(f1) > 1:  # if char repeats
            heappush(h, (f1 + 1, c1))  # push back with decrement frq

        if abs(f2) > 1:
            heappush(h, (f2 + 1, c2))  # push back with decrement frq

    if len(h) > 0:  # -------------------------------- NOTE [2]
        f, c = h[0]
        if abs(f) > 1:
            return ""  # this means we have something like h = [(2, "a")] which means there is no escape from repeating same char in text
        else:
            res += c
    return res