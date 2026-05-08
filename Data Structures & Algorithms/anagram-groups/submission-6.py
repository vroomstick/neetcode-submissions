class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            temp ="".join(sorted(s))

            if temp not in anagrams:
                anagrams[temp] = []

            anagrams[temp].append(s)


        return list(anagrams.values())

      

