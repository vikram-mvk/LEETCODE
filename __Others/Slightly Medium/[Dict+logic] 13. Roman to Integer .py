def romanToInt(self, s: str) -> int:
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = len(s) - 1
    ans = 0
    while i >= 0:
        ans = ans + d[s[i]]
        #at any point the numerical vallue corresponding to roman is added to ans
        #and then the corner case is checked.
        if i - 1 >= 0 and d[s[i - 1]] < d[s[i]]:
            # if previous element is smaller like in case of IV or IX we need to subtract
            ans = ans - d[s[i - 1]]
            i -= 1

        i -= 1
    return ans