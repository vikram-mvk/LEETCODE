'''
Question: Given an array of K values, find the minimum number of steps to go from 0 to K for each value
Only allowed operations are +1 or *2 at each step
return a res array containing Min steps for each K value
'''
def getMinOperations(kValues):
    res = []
    for k in kValues:
        start = 0
        end = k
        count = 0
        while end != 0:
            if end % 2 == 0:
                end = end // 2
            else:
                end -= 1
            count += 1
        res.append(count)

    return res
