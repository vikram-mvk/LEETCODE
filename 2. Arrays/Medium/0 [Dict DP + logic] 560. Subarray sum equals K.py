'''
#not an easy logic but understandable. Better to memorize
https://www.youtube.com/watch?v=HbbYPQc-Oo4&t=917s
Algo:
2 things to take care:
1. Update curr sum
2. Check curr sum == k to ensure if we've got a new sub array with the inclusion of current nums[i]
3. Check curr_sum - k is in pre_sums. If a sum that already exists occours,
it indicates that there is a new subarray with sum = k from that pre_sum's index to curr i
4. Update pre_sum by 1 if already seen or put its frequency as 1

'''

def subarraySum(self, nums, k: int) -> int:
    ans = 0
    pre_sums = {}
    curr_sum = 0
    for i in range(0, len(nums)):
        curr_sum = curr_sum + nums[i]
        if curr_sum == k:   ans += 1
        if curr_sum - k in pre_sums: ans += pre_sums[curr_sum - k]
        pre_sums[curr_sum] = 1 if curr_sum not in pre_sums else pre_sums[curr_sum] + 1

    return ans
'''

curr_sum simply adds up everything from 0 to i
pre_sums is a dictinary that stores all the sums before i and their frequency. Note that every sum is a contiguous sum.

We add ans, if at any point we find curr_sum equaling k.
We also check if curr_sum - nums[i] in pre_sum.
for ex: 3+4=7 at i=1
we add ans. then again when i=1.

Example: [3 4 7 2 -3 1 4 ] and k=7
curr_sum becomes 3 after i=0 and pre_sums[3] = 1 entry is made
now curr_sum is 7 which == k . so, ans=1
then curr_sum is 14 and 14-7 is in pre_sums so, add its frequency with existing ans
we do this because, if curr_sum-k == k, it means curr_sum is 2k. which indicates

Finally add the new curr_sum or incase it the same sum already has occoured, increment curr_sums frequency

(Testcase: [0,0,0,0,0,0,0,0,0,0] and k=0 ans is 55)

'''