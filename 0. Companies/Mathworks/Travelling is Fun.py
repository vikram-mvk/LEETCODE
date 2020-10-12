originCities=[1,2,4,6]
destinationCities=[3,3,3,4]
ans = []
g=1
i = j = 0
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

while i < len(originCities) and j < len(destinationCities):
    a=min(originCities[i], destinationCities[j])
    b=max(originCities[i], destinationCities[j])
    print(gcd(b,a))
    res = 1 if gcd(b, a) > g else 0
    ans.append(res)
    i += 1
    j += 1
print(ans)


