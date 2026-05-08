class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}

        for i in range(len(s)):
            if s[i] not in sHash:
                sHash[s[i]] = 1
            else:
                sHash[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in tHash:
                tHash[t[j]] = 1
            else:
                tHash[t[j]] += 1

        return sHash == tHash







    



        