'''
Solution one is Straight forward approach
The input limit is 4000
create arrays with all the possible values at each position. I.e., in units, tens, hundrends and thousands
units can be 1 2 3 4 ... 9
tens can be 10 20 30 ... 90
hundreds can be 100 200 300 ....900 etc.,
ex: take 26.
"" for both thousands and hundreds,
for tens, tens[2] =xx
for units, units[6]=VI
'''
#soln 1
def intToRoman(self, n: int) -> str:
    thousands = ["", "M", "MM", "MMM"];
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
    return thousands[n // 1000] + hundreds[(n % 1000) // 100] + tens[(n % 100) // 10] + units[n % 10];
    #modulo is done to prevent list index out of range. if 1994 is the number, the hundreth place will get index 19 if mod isn't used

#soln 2 is smart but could be slower
def intToRoman(self, num: int) -> str:
        #roman changing point is always at multiples of 5 and one minus those. 10 and 9. 50 and 40. etc.,
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV"]
        res = ""

        for i in range(len(val)):
            q = num // val[i] #divide the number
            if q == 0: continue #move to the point where quotient is greater than 0
            r = num % val[i]
            res += q * sym[i]
            num = r

        if num > 0:  res += num * "I"

        return res
