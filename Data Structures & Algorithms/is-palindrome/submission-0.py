class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        s = s.lower()

        for c in s:
            if c.isalnum():
                filtered += c

        #start pointers front and back of filtered
        #while pointers aren't equal 
        #if chars at pointers are equal then keep moving
        l = 0
        r = len(filtered) - 1
        while (l < r):
            if filtered[l] != filtered[r]:
                return False
            else:
                l += 1
                r -= 1

        return True