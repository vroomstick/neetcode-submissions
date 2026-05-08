class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        sHash, tHash = {}, {}

        for i in range(len(s)):
            if s[i] not in sHash:
                sHash[s[i]] = 0
            else:
                sHash[s[i]] += 1
            
            if t[i] not in tHash:
                tHash[t[i]] = 0
            else:
                tHash[t[i]] += 1

            

        return sHash == tHash
        






    



        