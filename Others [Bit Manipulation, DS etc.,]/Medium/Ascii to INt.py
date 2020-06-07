#using regex
import re

class Solution:
    def myAtoi(self, str: str) -> int:
        allNumbers = re.search("^(\s+)?([-+]?\d+)", str)
        if allNumbers == None:
            return 0
        else:
            finalNumber = int(float(allNumbers.group()))
            print(finalNumber)
            finalNumber = -2 ** 31 if finalNumber < -2 ** 31 else finalNumber
            finalNumber = (2 ** 31 - 1) if finalNumber > 2 ** 31 - 1 else finalNumber
            return finalNumber
#without regex
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()

        if not str:
            return 0

        isNeg = False
        pos = 0
        res = 0
        maxNum = (2 ** 31) - 1  # 2147483647
        minNum = -(2 ** 31)  # -2147483648

        if str[0] == "-":
            isNeg = True
            pos += 1

        if str[0] == "+":
            pos += 1

        while pos < len(str):
            if not str[pos].isdigit():
                break

            res = res * 10 + (ord(str[pos]) - ord('0'))
            pos += 1

        if isNeg:
            res = -res

        if res > maxNum:
            return maxNum
        if res < minNum:
            return minNum

        return res