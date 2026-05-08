from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        sHash, tHash = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            sHash[s[i]] += 1
            tHash[t[i]] += 1

        return sHash == tHash
        






    



        