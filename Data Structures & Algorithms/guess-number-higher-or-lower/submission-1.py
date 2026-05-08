# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 0, n

        while l <= h:
            m = l + (h - l) // 2
            r = guess(m)
            if r == 0:
                return m

            elif r == 1:
                l = m + 1

            elif r == -1:
                h = m - 1

            
        





        