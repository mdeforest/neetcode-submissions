class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1
        if x < 0:
            multiplier = -1

        xStr = str(abs(x))
        reversedStr = ""

        for i in range(len(xStr) - 1, -1, -1):
            reversedStr += xStr[i]

        reversedInt = int(reversedStr)
        if reversedInt > (2**31 - 1):
            return 0

        return reversedInt * multiplier