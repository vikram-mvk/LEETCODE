class Solution:
    def myAtoi(self, str: str) -> int:

        nums = str.strip()
        if len(nums) == 0: return 0
        flag = 1
        if 48 <= ord(nums[0]) <= 57 or nums[0] == "+" or nums[0] == "-":
            i = 0

            if ord(nums[0]) == 45:
                flag = -1
                i += 1
            if ord(nums[0]) == 43:  i += 1

            start = i

            while i < len(nums):
                if not (48 <= ord(nums[i]) <= 57): break
                i += 1

            if i == start: return 0

            ans = int(nums[start:i]) * flag
            if ans >= 2 ** 31: return (2 ** 31) - 1
            if ans <= -2 ** 31: return -2 ** 31
            return ans

        else:
            return 0


