'''
https://leetcode.com/problems/partition-labels/
'''
def partitionLabels(self, S: str) -> List[int]:
    d = {c: i for i, c in enumerate(S)}
    # By doing this we can get the last occurence of each character in the string

    last = d[S[0]]
    # We're intially setting the last occourence of 1st char as last to start the for loop

    ans = []
    start = 0

    # now, we have to scan each char
    for i, x in enumerate(S):
        # if some char's last occurence is greater, we need to go until we find that index before we can consider it as a partition
        if d[x] > last:
            last = d[x]

        # if we're in the last occourence of this partition, we can safely say that this is a partition.
        if i == last:
            ans.append(i - start + 1)
            # b-a+1 used to count length of interval, inclusive of the intervals
            start = last + 1
            # should not include the same interval. So +1
    return ans







