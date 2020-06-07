#One solution is to dynamically add items in set as we traverse, like in 2 sum and
# then checking if the compliment exist in previous elements in items
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        pairs, items = 0, set()
        if k == 0:
            d = {}
            for x in nums: d[x] = 1 if x not in d else d[x] + 1
            for val in d.values():
                if val > 1:   pairs += 1
            return pairs
        for i in nums:
            if i not in items and i - k in items: pairs += 1
            if i not in items and i + k in items: pairs += 1
            if i not in items: items.add(i)

        return pairs

#Another intuitive solution is to add a pair as a tuple in the set
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        pairs = set()
        items = set()

        for i in nums:
            if i - k in items and (i - k, i) not in pairs and (i, i - k) not in pairs: pairs.add((i - k, i))

            if i + k in items and (i + k, i) not in pairs and (i, i + k) not in pairs: pairs.add((i + k, i))

            if i not in items: items.add(i)

        return len(pairs)

#Another solution is to create a set of all numbers and then searching the compliment in that set
class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:  return 0
        res = 0
        if k == 0:
            d = {}
            for x in nums: d[x]=1 if x not in d else d[x]+1
            for val in d.values():
                if val > 1:   res += 1
            return res
        rec = set(nums)
        for key in rec:
            if key+k in rec:
                res += 1
        return res
#Another solution
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1: res += 1
        return res