'''
main idea is to update the end to current valid interval,
instead of reoving the largest interval, compare the current interval with the valid interval

'''
def eraseOverlapIntervals(intervals) -> int:
    if len(intervals)==0: return 0
    intervals =sorted(intervals,key=lambda x:x[0])
    valid_interval=intervals[0][1]
    i=1
    count=0
    while i<len(intervals):
        if valid_interval>intervals[i][0]: #merges at this point
            #instead of reomving the bigger interval, retain the smaller interval
            valid_interval=min(valid_interval,intervals[i][1])
            count+=1
        else:  valid_interval=intervals[i][1]
        i+=1
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))