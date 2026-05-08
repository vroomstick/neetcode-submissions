class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        firstWordHash, secondWordHash = {}, {}
        for i in range(len(s)):
            if s[i] not in firstWordHash.keys():
                firstWordHash[s[i]] = 1
            else:
                firstWordHash[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in secondWordHash.keys():
                secondWordHash[t[i]] = 1
            else:
                secondWordHash[t[i]] += 1
        print(firstWordHash)
        print(secondWordHash)

        for char in firstWordHash:
            if firstWordHash[char] != secondWordHash.get(char, 0):
                return False
        return True



        