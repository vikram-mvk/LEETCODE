def findJudge(N: int, trust) -> int:
    trusting = [0] * (N + 1)  # How many persons does this index (this person) is trusting
    trusted_by = [0] * (N + 1)  # How many persons are trusted by each index (index represents persons)
    for x in trust:
        trusting[x[0]] += 1
        trusted_by[x[1]] += 1
    for i in range(1, N + 1):
        if trusting[i] == 0 and trusted_by[i] == N - 1:  return i
    return -1
print(findJudge(2,[[1,2]]))